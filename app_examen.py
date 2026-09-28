import streamlit as st

# Configuración de la página web
st.set_page_config(page_title="Examen Consorcio", page_icon="🏢")

st.title("🏢 Simulador de Examen: Propiedad Horizontal (CABA)")
st.write("Respondé todas las preguntas y al final presioná el botón para ver tu nota.")
st.divider()

# La lista de preguntas
preguntas = [
    {
        "pregunta": "1. ¿Qué tipo de derecho real se ejerce sobre una unidad funcional según el artículo 2037 del CCyC?",
        "opciones": [
            "A) Un derecho real de usufructo exclusivo.",
            "B) Un derecho real sobre un inmueble propio, con una parte privativa y una indivisa común.",
            "C) Un derecho personal de uso y goce condicionado.",
            "D) Un derecho de superficie forestal y urbana."
        ],
        "correcta": "B"
    },
    {
        "pregunta": "2. ¿Cómo se define el Reglamento de Propiedad Horizontal desde su naturaleza jurídica?",
        "opciones": [
            "A) Como un contrato de adhesión que se integra al título y regula la vida consorcial.",
            "B) Como una ordenanza municipal optativa.",
            "C) Como un contrato de locación comercial.",
            "D) Como un acuerdo paritario con el SUTERH."
        ],
        "correcta": "A"
    },
    {
        "pregunta": "3. ¿Cuál es el requisito indispensable para que nazca jurídicamente el Reglamento?",
        "opciones": [
            "A) Aprobación por unanimidad en asamblea extraordinaria.",
            "B) Notificación por carta documento.",
            "C) Escritura pública e inscripción en el Registro de la Propiedad Inmueble.",
            "D) Homologación judicial en el fuero civil."
        ],
        "correcta": "C"
    },
    {
        "pregunta": "4. ¿Qué son las 'cosas comunes no indispensables' (Art. 2042 CCyC)?",
        "opciones": [
            "A) Cimientos, muros maestros y ascensores.",
            "B) Pileta, gimnasio, solárium, lavadero o SUM.",
            "C) Tabiques internos no portantes.",
            "D) El terreno y la estructura principal."
        ],
        "correcta": "B"
    },
    {
        "pregunta": "5. ¿Cómo se calculan ordinariamente las mayorías en la Asamblea de Propietarios?",
        "opciones": [
            "A) Por cantidad de personas presentes.",
            "B) Por partes proporcionales según los porcentuales de las unidades.",
            "C) Por decisión del Consejo de Propietarios.",
            "D) Por sorteo."
        ],
        "correcta": "B"
    },
    {
        "pregunta": "6. ¿Qué mayoría se requiere para modificar cláusulas esenciales del Reglamento?",
        "opciones": [
            "A) Mayoría simple de los presentes.",
            "B) 50% de los propietarios.",
            "C) Conformidad de todos los propietarios (unanimidad).",
            "D) 75% de los inquilinos."
        ],
        "correcta": "C"
    },
    {
        "pregunta": "7. Si no se convoca a asamblea anual, ¿pueden los propietarios autoconvocarse?",
        "opciones": [
            "A) No, es facultad exclusiva del administrador.",
            "B) Sí, con el apoyo de propietarios que representen al menos el 5% de partes proporcionales.",
            "C) Sí, con autorización de un juez.",
            "D) Sí, pero sin validez legal."
        ],
        "correcta": "B"
    },
    {
        "pregunta": "8. ¿Cuál es la función principal del Consejo de Propietarios?",
        "opciones": [
            "A) Reemplazar permanentemente al administrador.",
            "B) Controlar aspectos económicos, autorizar fondo de reserva y poder convocar asamblea.",
            "C) Modificar el reglamento unilateralmente.",
            "D) Dictar sentencias de desalojo."
        ],
        "correcta": "B"
    },
    {
        "pregunta": "9. ¿Qué figura jurídica describe al Administrador de un consorcio?",
        "opciones": [
            "A) Empleado de los inquilinos.",
            "B) Representante legal del consorcio (mandatario).",
            "C) Propietario absoluto de cosas comunes.",
            "D) Funcionario público de la Ciudad."
        ],
        "correcta": "B"
    },
    {
        "pregunta": "10. ¿Cuál es el plazo de prescripción por daños causados por el administrador?",
        "opciones": [
            "A) 1 año desde el fin del mandato.",
            "B) 2 años desde que asumió.",
            "C) 3 años desde que se conoció el daño.",
            "D) 10 años."
        ],
        "correcta": "C"
    },
    {
        "pregunta": "11. La naturaleza jurídica del Consorcio de Propietarios es:",
        "opciones": [
            "A) Sociedad comercial con fines de lucro.",
            "B) Persona jurídica privada, con capacidad y patrimonio propio (sin fines de lucro).",
            "C) Unión transitoria de vecinos.",
            "D) Entidad de bien público."
        ],
        "correcta": "B"
    },
    {
        "pregunta": "12. ¿Cómo se distribuyen habitualmente las expensas comunes?",
        "opciones": [
            "A) En partes iguales entre todos los departamentos.",
            "B) Según el porcentual de metros cuadrados fijado en el reglamento.",
            "C) Por cantidad de habitantes por unidad.",
            "D) Según el consumo de luz y gas."
        ],
        "correcta": "B"
    },
    {
        "pregunta": "13. ¿Cuál es el plazo habitual de pago de expensas?",
        "opciones": [
            "A) Del 1 al 5 de cada mes.",
            "B) Entre los 5 y 10 días del inicio del mes.",
            "C) A los 30 días.",
            "D) A fin de año."
        ],
        "correcta": "B"
    },
    {
        "pregunta": "14. ¿Qué genera la falta de pago de expensas?",
        "opciones": [
            "A) Pérdida automática de la propiedad.",
            "B) Corte de servicios de agua y luz.",
            "C) Intereses compensatorios y habilitación del cobro judicial.",
            "D) Prohibición de ingreso al edificio."
        ],
        "correcta": "C"
    },
    {
        "pregunta": "15. ¿Cómo se rige la relación laboral del personal del edificio?",
        "opciones": [
            "A) Ley de Contrato de Trabajo común exclusivamente.",
            "B) Obligatoriamente por el Convenio Colectivo de Trabajo del SUTERH.",
            "C) Por ordenanzas del Consejo de Propietarios.",
            "D) Como locación de servicios autónomos."
        ],
        "correcta": "B"
    },
    {
        "pregunta": "16. ¿Dónde se liquidan las cargas sociales (F931)?",
        "opciones": [
            "A) Ante la AFIP / ARCA.",
            "B) En el banco del SUTERH.",
            "C) En Rentas de la Ciudad.",
            "D) En el Colegio de Escribanos."
        ],
        "correcta": "A"
    },
    {
        "pregunta": "17. ¿Cuándo es el Día del Trabajador de Propiedad Horizontal?",
        "opciones": [
            "A) 1 de mayo.",
            "B) 2 de octubre.",
            "C) 12 de noviembre.",
            "D) Último viernes de noviembre."
        ],
        "correcta": "B"
    },
    {
        "pregunta": "18. ¿Qué es la rendición de cuentas del administrador?",
        "opciones": [
            "A) Un balance sin comprobantes.",
            "B) Documentación respaldada con facturas, recibos y contratos sobre ingresos y egresos.",
            "C) Declaración jurada de impuestos.",
            "D) Libro de sueldos visado."
        ],
        "correcta": "B"
    },
    {
        "pregunta": "19. ¿Son nulas las asambleas mal convocadas?",
        "opciones": [
            "A) No, si asiste el 80%.",
            "B) Sí, son nulas y sus decisiones pueden impugnarse judicialmente.",
            "C) No, es un error subsanable.",
            "D) Sí, pero solo las anula el administrador saliente."
        ],
        "correcta": "B"
    },
    {
        "pregunta": "20. ¿Qué es el fondo de reserva?",
        "opciones": [
            "A) Fondo (obligatorio o facultativo) para gastos imprevistos, a disposición del consorcio.",
            "B) Dinero para gastos personales del administrador.",
            "C) Está prohibido por el CCyC.",
            "D) Equivale al 100% de la recaudación mensual."
        ],
        "correcta": "A"
    }
]

# Usamos un formulario para que el usuario responda todo antes de evaluar
with st.form("formulario_examen"):
    respuestas_usuario = []
    
    for i, q in enumerate(preguntas):
        st.subheader(q["pregunta"])
        # st.radio crea las opciones para tildar
        respuesta = st.radio("Seleccioná tu opción:", q["opciones"], key=f"pregunta_{i}")
        respuestas_usuario.append(respuesta)
        st.write("---")
        
    # Botón de envío
    enviado = st.form_submit_button("Entregar Examen y Calcular Nota")

# Lógica de calificación (solo se ejecuta si se aprieta el botón)
if enviado:
    puntaje = 0
    total = len(preguntas)
    
    st.header("📊 Resultados del Examen")
    
    for i, q in enumerate(preguntas):
        # Tomamos solo la primera letra de la opción seleccionada (A, B, C o D)
        letra_elegida = respuestas_usuario[i][0]
        
        if letra_elegida == q["correcta"]:
            puntaje += 1
        else:
            st.error(f"❌ Error en la pregunta {i+1}. Elegiste la {letra_elegida}, pero la correcta era la {q['correcta']}.")
            
    nota = (puntaje / total) * 10
    
    st.success(f"Respuestas correctas: {puntaje} de {total}")
    st.info(f"⭐ Tu nota final es: {nota:.2f} / 10.00")
    
    if nota >= 7:
        st.balloons()
        st.write("🎉 **¡Aprobado! Excelente nivel de conocimiento.**")
    else:
        st.write("💪 **A seguir repasando, ¡la próxima sale mejor!**")
