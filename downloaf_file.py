import wget

print('Beginning file download with wget module')

url = 'https://geoservicos-hm.pbh.gov.br/geoserver/web/wicket/resource/org.geoserver.web.demo.MapPreviewPage/::/img/icons/geosilk/map-ver-3085230CE03A9A93A074669E4C194432.png'  
wget.download(url, 'cat4.jpg')  