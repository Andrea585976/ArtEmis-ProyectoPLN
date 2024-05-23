# Proyecto de Procesamiento del Lenguaje Natural: Análisis Emocional de Pinturas del Romanticismo

Este proyecto está inspirado en el trabajo de Panos Achlioptas et al. en "ArtEmis: Affective Language for Visual Art" [(arXiv:2101.07396)](https://arxiv.org/abs/2101.07396). La idea principal es desarrollar e implementar un modelo basado en transformers para analizar pinturas del período del Romanticismo y establecer conexiones emocionales con el espectador.

## Descripción

El objetivo de este proyecto es crear un modelo de aprendizaje automático capaz de generar descripciones emocionales y personales de pinturas del Romanticismo. A diferencia de las descripciones objetivas convencionales, nuestro modelo se centra en transmitir las emociones y las impresiones que una obra de arte puede evocar en un espectador. Esto se logra mediante el análisis del contenido visual de la pintura y la generación de texto que expresa las emociones percibidas.

## Inspiración en ArtEmis

ArtEmis es un modelo de aprendizaje que conecta las emociones humanas con obras de arte. Se basa en conjuntos de datos que contienen descripciones emocionales de imágenes visuales, lo que permite al modelo aprender asociaciones entre elementos visuales y estados emocionales. La arquitectura del modelo incluye el uso de embeddings para representar tanto las imágenes como las emociones, y una estructura de Codificador-Decodificador con Transformer para generar descripciones emocionales a partir de imágenes.

## Limitaciones y Alcance

Debido a limitaciones en los recursos computacionales, nuestro proyecto se enfoca en el análisis de pinturas del Romanticismo exclusivamente. Esta limitación nos permite profundizar en el análisis de un movimiento artístico específico y desarrollar un modelo más especializado y preciso. Sin embargo, en el futuro, podríamos expandir el alcance del proyecto para incluir otros períodos artísticos.

## Estructura del Modelo

Nuestro modelo se basa en la arquitectura general de ArtEmis, utilizando conjuntos de datos de pinturas del Romanticismo para entrenar y evaluar el modelo. La estructura del modelo incluye:

- **Conjuntos de Datos**: Utilizamos conjuntos de datos que contienen pinturas del Romanticismo junto con descripciones emocionales asociadas.
  
- **Embeddings**: Representamos tanto las imágenes de las pinturas como las emociones asociadas con embeddings, que capturan las características visuales y emocionales de manera vectorial.

- **Arquitectura Codificador-Decodificador con Transformer**: Implementamos una arquitectura de Codificador-Decodificador utilizando la arquitectura Transformer. El codificador procesa la imagen de la pintura y extrae características relevantes, mientras que el decodificador genera descripciones emocionales basadas en estas características.

- **Mecanismos de Atención**: Utilizamos mecanismos de atención para permitir que el modelo se centre en partes específicas de la imagen que son relevantes para la generación de descripciones emocionales.

## Contribución

Este proyecto tiene como objetivo contribuir al campo del procesamiento de lenguaje natural y la inteligencia artificial, proporcionando un enfoque innovador para el análisis emocional de obras de arte. Al comprender cómo las pinturas del Romanticismo pueden evocar emociones en los espectadores, esperamos abrir nuevas vías para la apreciación y comprensión del arte.

---

**Integrantes del Equipo:**
- Andrés Urbano Andrea
- Núñez Quintana Luis Axel
- Ramírez Gómez María Emilia
