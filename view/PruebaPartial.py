def probar_streamlit(st):
    """ Ponga aqui todos los controles de prueba para que entienda como funciona"""
    st.write("Agregue aquí botones, paneles, y opciones tal como se describe en el readme")
    st.button("Soy un boton")
    agree = st.checkbox('I agree')
    if agree:
        st.write('Great!')

    genre = st.radio(
        "What's your favorite movie genre",
        ('Comedy', 'Drama', 'Documentary'))

    if genre == 'Comedy':
        st.write('You selected comedy.')
    if genre == 'Drama':
        st.write('You selected Drama.')
    if genre == "Documentary":
        st.write("You selected Documentary.")

    option = st.selectbox(
        'How would you like to be contacted?',
        ('Email', 'Home phone', 'Mobile phone'))

    st.write('You selected:', option)


    st.line_chart({"data": [1, 5, 2, 6, 2, 1]})

    with st.expander("See explanation"):
        st.write("""
                The chart above shows some numbers I picked for you.
                I rolled actual dice for these, so they're *guaranteed* to
                be random.
            """)
        st.image("https://static.streamlit.io/examples/dice.jpg")