# Communes
Référentiel des communes de France

## Synopsis
Trouver le département, la région la population et la surface de la commune demandée en France

## Installation
```bash
kalliope install --git-url https://github.com/omoioli/communes.git
```

## Options

| Parameter   | Required | Type                             |
|-------------|----------|----------------------------------|
| nom_ville   | yes      | str                              |



## Return values

| Name            | Description                                  | Type   | Sample     |
|-----------------|----------------------------------------------|--------|------------|
| commune_asked   | Return the country of the given order        | string | 'auch'     |
| commune         | Return the country of the response           | string | 'Auch'     |
| code_post       | return the 'code postal'                     | string | '32260'    |
| surface         | return the surface in m² of the country      | string | '7345.92'  |                
| population      | return the people number of the country      | string | '21618'    |
| code_department | return the 'departement' code                | string | '32'       |
| department      | return the 'departement' name                | string | 'Gers'     |
| region          | return the 'région' name                     | string | 'Occitanie'|

## Notes
- if a country has multiple of 'code postal', only the first has dict
- if the country doesn't exist, the neuron return 'inconnue' for each value 

## Synapses example
```
  - name: "code-commune"
    signals:
      - order: "parle moi de {{ ville }}"
    neurons:
      - communes:
          nom_ville: "{{ ville }}"
          say_template: "la ville demandée est {{ code_post }} {{ commune }} dans le département {{ departement }}, {{ code_departement }}, région {{ region }}. {{ population }} habitants sur {{ surface }} mètres carrés."

```
