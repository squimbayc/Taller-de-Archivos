from urllib.request import urlopen

url = "https://blog.qupos.com/recomendaciones-para-minisuper-supermercados-covid-19" #Recomendaciones para minisúper y supermercados en contexto de COVID-19
page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")
indice_final = 0
Recomd_para_supermercados_Covid19 = []
print("Recomendaciones para supermercados en contexto de COVID-19")
contador = 1
for i in range(13):
    lineamientos = html.find('<p><span style="color: #000000;">')
    indice_inicial = lineamientos + len('<p><span style="color: #000000;">')
    indice_final = html.find("</span></p>")

    title = html[indice_inicial:indice_final]

    if i != 4:
        print(str(contador) + ".", title)
        Recomd_para_supermercados_Covid19.append(title)
        contador = contador + 1


    nueva_html = len(html[:indice_final + 11])
    html = html[nueva_html:]
