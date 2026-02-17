import streamlit as st

# Настройка страницы (убираем лишнее, скрываем сайдбар)
st.set_page_config(
    page_title="Прогноз САД",
    initial_sidebar_state="collapsed"
)

# --- CSS Стилизация (чтобы выглядело как на скриншоте) ---
st.markdown("""
    <style>
    /* Скрываем стандартное меню и футер */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Центрируем заголовок */
    h1 {
        text-align: center;
        font-size: 26px;
        font-weight: 700;
        margin-bottom: 30px;
        color: #000;
    }
    
    /* Стилизация заголовков полей ввода */
    .input-label {
        font-weight: 600;
        font-size: 16px;
        margin-bottom: 5px;
    }

    /* Зеленая кнопка "Рассчитать" во всю ширину */
    div.stButton > button {
        width: 100%;
        background-color: #28a745; /* Зеленый цвет */
        color: white;
        font-weight: bold;
        font-size: 18px;
        border: none;
        border-radius: 5px;
        padding: 10px 0;
        margin-top: 10px;
    }
    div.stButton > button:hover {
        background-color: #218838; /* Темно-зеленый при наведении */
        color: white;
        border: none;
    }
    div.stButton > button:active {
        background-color: #1e7e34;
        color: white;
    }

    /* Серое поле результата */
    .result-container {
        background-color: #e9ecef; /* Светло-серый фон */
        padding: 20px;
        border-radius: 5px;
        margin-top: 20px;
        font-size: 18px;
        color: #000;
    }
    </style>
""", unsafe_allow_html=True)

# --- Заголовок ---
st.markdown("<h1>Прогнозирование значение систолического артериального давления перед операцией</h1>", unsafe_allow_html=True)

# --- Поля ввода ---

# 1. Вес
st.markdown('<div class="input-label">Вес пациента (кг)</div>', unsafe_allow_html=True)
weight = st.number_input(
    "Вес", 
    min_value=30.0, 
    max_value=250.0, 
    value=70.0, 
    step=0.5, 
    label_visibility="collapsed" # Скрываем стандартный лейбл, используем свой CSS выше
)

# Отступ
st.write("") 

# 2. Обезвоживание
st.markdown('<div class="input-label">Наличие обезвоживания</div>', unsafe_allow_html=True)
dehydration_str = st.selectbox(
    "Обезвоживание", 
    options=["Нет", "Да"], 
    label_visibility="collapsed"
)

# --- Логика расчета ---
# Преобразуем выбор в цифры: Нет=0, Да=1
dehydration_val = 1 if dehydration_str == "Да" else 0

# Формула: 109.725 + 0.219*Вес + 8.515*Наличие
prediction = 109.725 + (0.219 * weight) + (8.515 * dehydration_val)

# --- Кнопка и Результат ---
if st.button("Рассчитать"):
    st.markdown(f"""
        <div class="result-container">
            <b>Результат прогноза САД:</b><br>
            <span style="font-size: 24px; font-weight: bold;">{prediction:.2f} мм рт. ст.</span>
        </div>
    """, unsafe_allow_html=True)
