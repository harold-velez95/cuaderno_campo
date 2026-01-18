document.addEventListener("DOMContentLoaded", function () {

  const map = L.map('map').setView([40.0, -3.5], 6);

  L.tileLayer(
    'https://server.arcgisonline.com/ArcGIS/rest/services/' +
    'World_Imagery/MapServer/tile/{z}/{y}/{x}',
    {
      attribution: '© Esri, Maxar, Earthstar Geographics'
    }
  ).addTo(map);

  let currentLayer = null;

  function consultarRecinto() {
    const provincia = document.getElementById('provincia')?.value;
    const municipio = document.getElementById('municipio')?.value;
    const agregado = document.getElementById('agregado')?.value;
    const zona = document.getElementById('zona')?.value;
    const poligono = document.getElementById('poligono')?.value;
    const parcela = document.getElementById('parcela')?.value;
    const recinto = document.getElementById('recinto')?.value;

    if (!provincia) {
      console.warn("Campos no disponibles aún");
      return;
    }

    const filter =
      `provincia=${provincia} AND municipio=${municipio}` +
      ` AND agregado=${agregado} AND zona=${zona}` +
      ` AND poligono=${poligono} AND parcela=${parcela}` +
      ` AND recinto=${recinto}`;

    const url =
      "https://sigpac-hubcloud.es/ogcapi/collections/recintos/items?f=json" +
      "&filter=" + encodeURIComponent(filter);

    fetch(url)
      .then(r => r.json())
      .then(data => {
        if (!data.features || data.features.length === 0) {
          alert("No se encontró el recinto con esos parámetros.");
          return;
        }

        if (currentLayer) {
          map.removeLayer(currentLayer);
        }

        currentLayer = L.geoJSON(data, {
          style: {
            color: 'blue',
            weight: 2,
            fillOpacity: 0.3
          },
          onEachFeature: (feature, layer) => {
            const p = feature.properties;
            const uso = p.desc_uso_sigpac || p.uso_sigpac || "No disponible";
            const superficie = p.superficie_ha || p.superficie || "No disponible";

            layer.bindPopup(`
              <b>Uso del suelo:</b> ${uso}<br>
              <b>Superficie:</b> ${superficie} ha
            `);
          }
        }).addTo(map);

        map.fitBounds(currentLayer.getBounds());
      })
      .catch(err => {
        console.error("Error:", err);
        alert("Hubo un error al consultar la API.");
      });
  }

  // 🔥 EJECUCIÓN AUTOMÁTICA AL ENTRAR
  consultarRecinto();

});
