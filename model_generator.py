import streamlit as st
import webbrowser #pour ouvrir les pages web 
import pyvista as pv
import time
def generate_url(sex=0, bust=90.4, underbust=80.6, waist=80.2, hip=98.3, 
        neckgirth=33.4, insideleg=76.3, shoulder=36.6, bodyheight=188.0):
    url = 'https://raniabenabdallah-a.github.io/3DModelApp/'
    url += 'sex=' + str(sex)
    url += '&Bust=' + str(bust)
    url += '&UnderBust=' + str(underbust)
    url += '&Waist=' + str(waist)
    url += '&Hip=' + str(hip)
    url += '&NeckGirth=' + str(neckgirth)
    url += '&InsideLeg=' + str(insideleg)
    url += '&Shoulder=' + str(shoulder)
    url += '&BodyHeight=' + str(bodyheight)

    return url


def generate_model(url):
    webbrowser.open_new_tab(url)

def display_model_in_streamlit(url):
    plotter = pv.Plotter(notebook=False)
    mesh = pv.read(url)
    plotter.add_mesh(mesh, color='white', smooth_shading=True)
    st.pyvista_plot(plotter, use_container_width=True)

def main():
    model_url = generate_url()
    generate_model(model_url)
    display_model_in_streamlit(model_url)

if __name__ == '__main__':
    main()