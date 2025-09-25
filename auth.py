import streamlit as st
from auth import login, logout
from ui_admin import admin_inventario_ui, admin_historial_ui, admin_delivery_ui
from ui_empleado import empleado_inventario_ui, empleado_delivery_ui
# Importa otras funciones necesarias

# Configuración de la página
st.set_page_config(page_title="Sistema de Inventario", layout="wide")

# Funciones para cargar y guardar datos (aquí irían tus funciones)

def main():
    # Verificar autenticación
    usuario, rol = login()
    
    # Mostrar la interfaz solo si el usuario está autenticado
    if usuario:
        # Mostrar un botón de cierre de sesión en la barra lateral
        if st.sidebar.button("Cerrar sesión"):
            usuario, rol = logout()
            st.experimental_rerun()
        
        st.sidebar.write(f"Usuario: {usuario}")
        st.sidebar.write(f"Rol: {rol}")
        
        # Mostrar la interfaz según el rol
        if rol == "administrador":
            menu = st.sidebar.radio(
                "Menú Administrador",
                ["Inventario", "Historial", "Delivery"]
            )
            
            if menu == "Inventario":
                inventario = cargar_inventario()  # Tu función para cargar datos
                admin_inventario_ui(inventario)
            elif menu == "Historial":
                historial = cargar_historial()  # Tu función para cargar historial
                admin_historial_ui(historial)
            elif menu == "Delivery":
                admin_delivery_ui(cargar_catalogo_delivery, guardar_catalogo_delivery, cargar_ventas_delivery)
        
        elif rol == "empleado":
            menu = st.sidebar.radio(
                "Menú Empleado",
                ["Inventario", "Delivery"]
            )
            
            if menu == "Inventario":
                inventario = cargar_inventario()  # Tu función para cargar datos
                opciones_valde = {"Vacío": 0, "Lleno": 1}  # Tus opciones de baldes
                empleado_inventario_ui(inventario, usuario, opciones_valde, guardar_inventario, guardar_historial)
            elif menu == "Delivery":
                empleado_delivery_ui(usuario, cargar_catalogo_delivery, guardar_venta_delivery, cargar_ventas_delivery)

if __name__ == "__main__":
    main()
