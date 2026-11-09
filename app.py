import streamlit as st

st.set_page_config(
    page_title="Permanencia IA",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Permanencia IA")
st.subheader("Prototipo de alertas tempranas de riesgo de deserción universitaria")
st.info(
    "Prototipo académico demostrativo. Utiliza reglas ilustrativas y datos ingresados "
    "por el usuario; no es un modelo de IA entrenado ni produce probabilidades reales."
)

st.markdown(
    "Registra un **caso ficticio** para observar cómo la herramienta podría organizar "
    "señales de alerta y sugerir acciones de acompañamiento."
)

with st.form("student_form"):
    st.header("1. Información académica y de contexto")
    col1, col2 = st.columns(2)

    with col1:
        promedio = st.slider("Promedio académico (escala de 0 a 5)", 0.0, 5.0, 3.2, 0.1)
        asistencia = st.slider("Porcentaje de asistencia", 0, 100, 85, 1)
        materias_perdidas = st.number_input(
            "Asignaturas perdidas en el último período",
            min_value=0, max_value=15, value=0, step=1
        )
        creditos_aprobados = st.selectbox(
            "¿Ha disminuido la aprobación de créditos?",
            ["No", "Sí", "No sabe"]
        )

    with col2:
        dificultad_economica = st.selectbox(
            "¿Reporta dificultades económicas?",
            ["No", "Sí", "No sabe"]
        )
        trabaja = st.selectbox(
            "¿Debe trabajar mientras estudia?",
            ["No", "Sí", "Prefiere no responder"]
        )
        apoyo = st.selectbox(
            "¿Cuenta con acompañamiento académico o institucional?",
            ["Sí", "No", "No sabe"]
        )
        situacion_personal = st.selectbox(
            "¿Reporta alguna situación personal que afecte sus estudios?",
            ["No", "Sí", "Prefiere no responder"]
        )

    submitted = st.form_submit_button("Analizar caso")

if submitted:
    score = 0
    factores = []
    recomendaciones = []

    # Reglas transparentes e ilustrativas; deben calibrarse con datos reales.
    if promedio < 3.0:
        score += 25
        factores.append("Promedio académico inferior a 3,0.")
        recomendaciones.append("Ofrecer tutorías, monitorías o acompañamiento en las asignaturas de mayor dificultad.")
    elif promedio < 3.5:
        score += 12
        factores.append("Promedio académico que podría requerir seguimiento.")
        recomendaciones.append("Realizar seguimiento académico y revisar la evolución del promedio.")

    if asistencia < 70:
        score += 20
        factores.append("Asistencia inferior al 70%.")
        recomendaciones.append("Contactar al estudiante para comprender las causas de las inasistencias y acordar un plan de seguimiento.")
    elif asistencia < 85:
        score += 10
        factores.append("Asistencia entre 70% y 84%.")
        recomendaciones.append("Monitorear la asistencia durante el siguiente período.")

    if materias_perdidas >= 3:
        score += 20
        factores.append("Tres o más asignaturas perdidas.")
        recomendaciones.append("Priorizar asesoría académica y revisar posibles ajustes en la carga académica.")
    elif materias_perdidas >= 1:
        score += 10
        factores.append("Al menos una asignatura perdida.")
        recomendaciones.append("Identificar las asignaturas con dificultades y ofrecer apoyo oportuno.")

    if dificultad_economica == "Sí":
        score += 15
        factores.append("Dificultades económicas reportadas.")
        recomendaciones.append("Orientar sobre becas, subsidios, financiación y apoyos socioeconómicos disponibles.")

    if trabaja == "Sí":
        score += 5
        factores.append("Compatibiliza trabajo y estudio.")
        recomendaciones.append("Explorar alternativas de horarios, carga académica y orientación para organizar el tiempo.")

    if apoyo == "No":
        score += 10
        factores.append("No cuenta con acompañamiento académico o institucional.")
        recomendaciones.append("Asignar un canal de contacto o referente de acompañamiento institucional.")

    if situacion_personal == "Sí":
        score += 10
        factores.append("Reporta una situación personal que puede afectar sus estudios.")
        recomendaciones.append("Ofrecer orientación confidencial y, si el estudiante lo desea, remisión a bienestar universitario.")

    score = min(score, 100)

    if score >= 60:
        nivel = "Alto"
        color = "error"
        explicacion = "El caso reúne varias señales que ameritan priorizar una revisión humana y un contacto oportuno."
    elif score >= 30:
        nivel = "Medio"
        color = "warning"
        explicacion = "Se observan señales que justifican seguimiento preventivo."
    else:
        nivel = "Bajo"
        color = "success"
        explicacion = "Con la información ingresada se observan pocas señales de alerta. Conviene mantener el seguimiento habitual."

    st.divider()
    st.header("2. Resultado del análisis demostrativo")

    c1, c2 = st.columns(2)
    c1.metric("Índice ilustrativo de alertas", f"{score}/100")
    c2.metric("Nivel de alerta", nivel)

    st.progress(score / 100)
    st.write(explicacion)

    st.subheader("Factores identificados")
    if factores:
        for factor in factores:
            st.write(f"- {factor}")
    else:
        st.write("No se identificaron factores de alerta según las reglas ilustrativas.")

    st.subheader("Recomendaciones sugeridas")
    if recomendaciones:
        for recomendacion in dict.fromkeys(recomendaciones):
            st.write(f"- {recomendacion}")
    else:
        st.write("- Mantener los canales de acompañamiento y el seguimiento académico habitual.")

    st.caption(
        "Importante: el índice es una puntuación heurística creada para demostrar el flujo "
        "del prototipo. No equivale a una probabilidad de deserción, no ha sido validada "
        "estadísticamente y no debe utilizarse para tomar decisiones reales sobre estudiantes."
    )

st.divider()
st.header("3. Alcance y próximos pasos")
st.markdown(
    """
    **Lo que demuestra este prototipo**
    - Recibe variables académicas y de contexto.
    - Aplica reglas transparentes para organizar señales de alerta.
    - Presenta un nivel de alerta ilustrativo.
    - Sugiere acciones de acompañamiento relacionadas con los factores ingresados.

    **Lo que falta para una implementación real**
    - Validar las variables con estudiantes, docentes y áreas de bienestar.
    - Obtener datos históricos autorizados y protegidos.
    - Entrenar y evaluar un modelo predictivo con métricas como sensibilidad,
      especificidad y precisión.
    - Revisar sesgos, explicabilidad, privacidad y supervisión humana.
    """
)
