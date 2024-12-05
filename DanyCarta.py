import streamlit as st
from PIL import Image
import base64
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Dany, eres mi casualidad", page_icon=":love_letter:", layout="wide")
hide_st_style = """
<style>
#MainMenu {
  visibility: hidden;
  }
footer {
  visibility: hidden;
  }
header {
  visibility: hidden;
}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

selected = option_menu(None, ["Portada","Carta"],
          icons=["person-vcard", "folder-fill"],
          menu_icon="cast", default_index=0, orientation="horizontal")


if selected =="Portada":
  # Convertir imagen a base64
  def image_to_base64(img_path):
      with open(img_path, "rb") as f:
          return base64.b64encode(f.read()).decode()
  
  # Imagen de portada
  cover_image = image_to_base64('portadapaloma.PNG')
  
  st.markdown(f"""
          <style>
          .stApp {{
              background-image: url('data:image/jpeg;base64,{cover_image}');
              background-size: cover;
          }}
          </style>
      """, unsafe_allow_html=True)

if selected =="Carta":
    def image_to_base64(img_path):
        with open(img_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
          
    background_image = image_to_base64('fondo1.jpg')
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url('data:image/jpeg;base64,{background_image}');
            background-size: cover;
        }}
        </style>
    """, unsafe_allow_html=True)

    # Contenido de la carta
    st.markdown('<p style="color: black; font-size: 36px;"><strong>Querida Dany,</strong></p>', unsafe_allow_html=True)

    st.markdown('<p style="color: black; font-size: 18px;">"Eres la casualidad más bonita que llegó a mi vida."</p>', unsafe_allow_html=True)

    introduccion = '''Quise empezar con esa frase porque siento que expresa de la mejor manera todo lo que te quiero decir. Desde que te conocí, no hago más que pensar en ti. Por ejemplo, mientras veo alguna película o serie, no puedo evitar imaginar tus reacciones o pensar qué estarás haciendo. Cada vez que estoy contigo, siento una tranquilidad y felicidad difícil de explicar.'''
    st.markdown(f'<p style="color: black;">{introduccion}</p>', unsafe_allow_html=True)

    cuando_te_vi1 = '''Aún recuerdo la primera vez que te vi. No sé si crees en las conexiones especiales, pero desde que te conocí, siento que la vida quiso sorprenderme contigo. En esa fiesta estuve a punto de no ir porque mis amigos me cancelaron a última hora, pero al final me animé, y fue la mejor decisión, porque gracias a ello pude conocerte.'''
    st.markdown(f'<p style="color: black;">{cuando_te_vi1}</p>', unsafe_allow_html=True)

    cuando_te_vi2 = '''A pesar de que iba de Anakin y había una Padmé en la fiesta, la persona que realmente quería conocer eras tú. Ibas de negro y te veías tan hermosa a mis ojos. En un momento, dijiste: “¿Sabías que Anakin fue mi crush de la infancia?”. Me quedé sin palabras y sin saber cómo reaccionar. Después, me preguntaste: “Oye, ¿cómo me veo? ¿Me veo peda?”. A pesar de que te dije que no, seguiste preguntando. Incluso me acompañaste a recibir unas bebidas, y fue ahí cuando le preguntaste lo mismo al del Uber. Me sacaste una risa que solo hacía que me fijara más en ti.'''
    st.markdown(f'<p style="color: black;">{cuando_te_vi2}</p>', unsafe_allow_html=True)

    cuando_te_vi3 = '''Esa noche seguías viniendo a preguntarme lo mismo, y solo me arrepiento de una cosa, no tener el valor para pedirte tu número directamente. Por fortuna, al día siguiente, abrí mi galería y encontré unas fotos y un video de ti. Fue entonces cuando decidí arriesgarme.'''
    st.markdown(f'<p style="color: black;">{cuando_te_vi3}</p>', unsafe_allow_html=True)

    me_gustas1 = '''Pero si te lo preguntas, no solo me gustas por tu hermosa sonrisa, sino también por tu forma de ser, me gusta que seas muy agradecida, me gusta como te pones tus objetivos y buscas cumplirlos, me gusta que eres fiel a tus valores y creencias, me gusta que siempre tratas de dar lo mejor de ti a pesar de tener tu agenda bien llena, me gusta como te pones nerviosa cuando te digo algo cursi, me encanta ver tus ojos, me gusta que te diviertes a tu manera, me gusta el valor que le das a tus amistades y la importancia de fechas especiales, me encantó que estuviste en mi cumple y más tu promesa del mensaje a las 12, ME GUSTAS TÚ y siento que entre más te conozco, más me enamoro.
    Sé que no te gustan mucho las promesas porque, cuando no se cumplen, pueden dejarte con expectativas rotas. Pero, más allá de una promesa, quiero demostrártelo día a día que tú eres la persona que me gusta y con quien quiero estar.'''
    st.markdown(f'<p style="color: black;">{me_gustas1}</p>', unsafe_allow_html=True)

    me_gustas2 = '''Sin embargo, quiero ser claro contigo. Mi intención no es apresurar nada, quiero conocerte mejor y que tú también me conozcas. Pero quiero que sepas que me gustaría algo más que una amistad contigo, si eso es algo que tú también quisieras. Si no es así, lo entenderé, pero creo que es mejor hablarlo para evitar malentendidos.
    Lo único que quiero es que te sientas cómoda y para mí, lo más importante es que seas tú misma conmigo, igual que yo lo soy contigo. "Solo imagina lo precioso que puede ser arriesgarse y que todo salga bien. — Mario Benedetti."'''
    st.markdown(f'<p style="color: black;">{me_gustas2}</p>', unsafe_allow_html=True)

    cancion = '''P.D.: Te dedico esta canción'''
    st.markdown(f'<p style="color: black;">{cancion}</p>', unsafe_allow_html=True)

    # Insertando el código de Spotify
    spotify_embed_code = """
    <iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/3zNcn4BaVfKORyx3uDfruW?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
    """
    st.components.v1.html(spotify_embed_code, height=352)

    respuesta = '''P.D.2: Me hubiera encantado ver tu reacción en persona, pero espero tu selfie. Y si tienes algo que decirme, estaré feliz de escucharte o leerte'''
    st.markdown(f'<p style="color: black;">{respuesta}</p>', unsafe_allow_html=True)
  
    firma = '''Con cariño,'''
    st.markdown(f'<p style="color: black; font-size: 24px;">{firma}</p>', unsafe_allow_html=True)

    autor = '''Tu Anakin Skywalker''' 
    st.markdown(f'<p style="color: black; font-size: 20px;">{autor}</p>', unsafe_allow_html=True)
