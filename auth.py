# Logica y datos de usuarios
import streamlit as st

usuarios = {
    'empleado1': 'empleado',
    'empleado2': 'empleado',
    'empleado3': 'empleado',
    'admin1': 'administrador'
}

def login():
    # Inicializar variables de sesión si no existen
    if 'usuario_autenticado' not in st.session_state:
        st.session_state.usuario_autenticado = None
        st.session_state.rol_usuario = None
    
    # Si ya hay un usuario autenticado, devolver sus datos
    if st.session_state.usuario_autenticado:
        return st.session_state.usuario_autenticado, st.session_state.rol_usuario
    
    # Usar columnas para centrar el formulario
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.title("Inicio de sesión")
        usuario = st.text_input("Usuario")
        password = st.text_input("Contraseña", type="password")
        login_button = st.button("Ingresar")
        
        if login_button:
            if usuario in usuarios:
                st.session_state.usuario_autenticado = usuario
                st.session_state.rol_usuario = usuarios[usuario]
                st.success(f"Hola {usuario}, rol: {st.session_state.rol_usuario}")
            else:
                st.error("Usuario no reconocido")
    
    # Devolver el estado actual (autenticado o no)
    return st.session_state.usuario_autenticado, st.session_state.rol_usuario

def logout():
    st.session_state.usuario_autenticado = None
    st.session_state.rol_usuario = None
    return None, None
