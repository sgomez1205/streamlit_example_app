"""Instructions"""


def consultar_instrucciones(st):
    st.title("Primera Vez usando Streamlit")
    st.write("Primera oportunidad tras utilizar streamlit, donde se muestra "
             "el inicio de uso del framework, puede ser utilizado para hacer paginas web.")
    code = '''def hello():
         print("Hello, Streamlit!")'''
    st.code(code, language="python")
    return 0
