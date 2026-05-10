Chatbot inteligente para una agencia de autos ficticia que responde preguntas sobre financiamiento, mensualidades y catálogo de vehículos a partir de un documento PDF.
 
Proyecto desarrollado para la materia de **Finanzas** — FES Acatlán, UNAM.
 
---
 
## ¿Qué hace?
 
- Lee y extrae información de un catálogo PDF de la agencia
- Responde preguntas en lenguaje natural sobre autos, precios y créditos
- Calcula mensualidades usando la fórmula de amortización financiera
- Usa un modelo de lenguaje (LLaMA 3 vía Groq) para entender las preguntas
---
 
## Ejemplo de preguntas
 
> *"¿Cuánto pagaría mensual por el Aveo a 24 meses con 20% de enganche?"*
 
> *"¿Qué tasa de interés tienen para seminuevos?"*
 
> *"¿Qué documentos necesito para solicitar el crédito?"*
 
> *"¿Tienen SUVs disponibles?"*
 
---
 
## Tecnologías usadas
 
| Herramienta | Para qué |
| Python | Lenguaje principal |
| Streamlit | Interfaz web del chatbot |
| pdfplumber | Extracción de texto del PDF |
| Groq API | Modelo de lenguaje (LLaMA 3.3) |
| python-dotenv | Manejo seguro de la API key |
 
---
