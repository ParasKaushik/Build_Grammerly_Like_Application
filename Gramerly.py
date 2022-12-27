from gingerit.gingerit import GingerIt
import cloudscraper
import streamlit as st

st.title('Sasta Grammerly')
text= st.text_area("Enter Text...",value='',height=None , max_chars=None,key=None)
parser=GingerIt()
if st.button('Correct Sentence'):
    if text=='':
        st.write('Place Enter Text')
    else:
        result_dict=parser.parse(text)
        st.markdown('**Corrected Sentece** '+str(result_dict["result"]))
else:
    pass
