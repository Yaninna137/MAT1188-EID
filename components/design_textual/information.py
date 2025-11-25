
'''
Contenido estatico, aca se ingresa los texto de cada seccion y ser llamados 
en su respectiva pagina.
'''
def Header_subheader():
  Contenido = '''
      <h1 style="text-align:center;">MAT1188 - Sistema EID</h1>
      <h4 style="text-align:center; color:gray; font-weight:400;">
          Aplicación de Derivadas e Integrales
      </h4>
  '''
  return Contenido

def SectionBOX1():
    return '''
    <section class="card card-info" id="box1">
        <h2 class="h2box1">1. Situación Problema</h2>
        <p>
            En ingeniería informática, los servidores representan un recurso
            crítico. Con el tiempo, su costo de mantención aumenta debido a
            fallas, recalentamiento, desgaste físico y pérdida de eficiencia
            energética. Este comportamiento puede modelarse matemáticamente para
            estimar:
        </p>
        <ul>
            <li>El ritmo al que aumentan los costos de mantención (derivada).</li>
            <li>El costo acumulado de operar el servidor por varios años (integral).</li>
            <li>El punto óptimo para reemplazar el hardware.</li>
        </ul>
        <p>
            Esta aplicación parte de un escenario real dentro de la ingeniería
            informática: el aumento progresivo del costo de mantener un servidor a
            lo largo del tiempo. Factores como desgaste del hardware, fallas
            recurrentes, mayor consumo energético y pérdida de eficiencia generan
            un comportamiento creciente en los costos. Este fenómeno puede
            modelarse matemáticamente para analizar tasas de variación y
            acumulación, permitiendo tomar decisiones informadas sobre mantención
            o reemplazo.
        </p>
    </section>
    '''


def SectionBOX2():
    return '''
    <section class="card card-secondary" id="box2">
        <h2 class="h2box2">Configuración del Modelo</h2>
        <p>El usuario puede controlar los siguientes parámetros:</p>
        <ul>
            <li><strong>C(t):</strong> Función editable del costo mensual.</li>
            <li><strong>Periodo de amortización T</strong></li>
            <li><strong>Opcionales:</strong>
                <ul>
                    <li>Tasa de descuento r</li>
                    <li>Costo de reemplazo K</li>
                </ul>
            </li>
        </ul>
    </section>
    '''

def SectionBOX3(exprecion):
   return f'''
      <section class="BOX-3">
        <h2>2. Función Matemática</h2>
        <p>
          Esta función representa el costo mensual de mantener el servidor en
          función del tiempo:
        </p>

        <div class="formula">{exprecion}</div>

        <!-- NUEVA DESCRIPCIÓN -->
        <p>
          Para representar el fenómeno descrito, se define una función C(t) que
          modela el costo mensual de mantención del servidor en función del
          tiempo t. Esta función captura el crecimiento progresivo del gasto a
          medida que el hardware envejece o se deteriora. El usuario puede
          modificar la función para simular distintos escenarios o tipos de
          servidores.
        </p>

        <h3>Gráfico de C(t)</h3>
        <div class="graph-placeholder">[Gráfico de C(t)] </div>  <!-- BORRAR CUANDO SE implemente el grafico -->
      </section>'''

def SectionBOX4(formulaStr, formula): # formulaStr es la que se muestra, formula es la q se analiza
   import sympy as sp   # se pasa a sympy para analizar la expresion
   t = sp.symbols('t')
   expresion_analizable = sp.sympify(formula) # Esta expresión será la derivada
   constante = expresion_analizable.coeff(t,0)  # Obtener el término constante de la derivada
   grado = sp.degree(expresion_analizable, gen=t)  # Obtener el grado de la derivada
   coeficiente_mayor = expresion_analizable.coeff(t, grado)  # Coeficiente del término de mayor grado

   # Ceros de la derivada
   ceros = sp.solve(expresion_analizable, t)
   segunda_derivada = sp.diff(expresion_analizable, t)
   puntos_criticos = []
   for cero in ceros:
        if not cero.is_real:
            continue  # Ignorar ceros complejos, no afectan el análisis real

        if cero > 0:  # Solo considerar ceros positivos
          valor_segunda = segunda_derivada.subs(t, cero)
          if valor_segunda > 0:
              puntos_criticos.append((cero, "mínimo"))
          elif valor_segunda < 0:
              puntos_criticos.append((cero, "máximo"))
          else:
              puntos_criticos.append((cero, "punto de inflexión"))
     # Interpretación de puntos críticos
   interpretacion_puntos = ""
   if puntos_criticos:
       interpretacion_puntos += "Los puntos críticos encontrados son: <br />"
       for punto, tipo in puntos_criticos:
        latex_punto = sp.latex(punto)
        interpretacion_puntos += f"$t = {latex_punto}$ es un {tipo}. <br />"
   else:
       interpretacion_puntos = "No se encontraron puntos críticos para t positivos, por lo tanto no hay máximos ni mínimos relevantes en el intervalo considerado.<br />"

   if grado == 1:
       interpretacion = f"La derivada es una función lineal, indicando un {'crecimiento' if coeficiente_mayor > 0 else 'decrecimiento'} constante de {coeficiente_mayor} en la tasa de crecimiento del costo. El término constante {constante} representa el punto inicial en el que luego el costo {"crece" if coeficiente_mayor > 0 else "disminuye"}."
   elif grado == 0:
        interpretacion = f"La derivada es una constante ({constante}), indicando que el costo de mantenimiento aumenta a una tasa fija de {constante} cada año."
   else:
        interpretacion = f"La derivada es una función polinómica de grado {grado}, indicando que la tasa de crecimiento del costo varía con el tiempo. "
        if coeficiente_mayor > 0:
            interpretacion += "El coeficiente positivo del término de mayor grado sugiere que la tasa de aumento del costo se acelera con el tiempo."
        elif coeficiente_mayor < 0:
            interpretacion += "El coeficiente negativo del término de mayor grado sugiere que la tasa de aumento del costo se desacelera con el tiempo."

   return [f'''
      <section class="BOX-4">
        <h2>3. Análisis con Derivadas</h2>

        <p>
          En esta sección se aplica la derivada de la función de costo para
          estudiar cómo cambia el gasto con el tiempo. La derivada permite
          analizar tasas de variación, identificar momentos donde los costos
          crecen más rápido y evaluar posibles máximos o mínimos relevantes para
          el comportamiento del sistema.
        </p>

        $${formulaStr}$$

      </section>
        ''', f'''
      <section class="BOX-4">
        <p>
          Interpretación:
          <br />• {interpretacion} <br />
        </p>


        {interpretacion_puntos}

        
        <br />
        <h3>Gráfico de C'(t)</h3>
        <div class="graph-placeholder">[Gráfico de C'(t)]</div> <!-- BORRAR CUANDO SE implemente el grafico -->
      </section>
''']
def SectionBOX5(expresionA,expresionB):
   return f'''
      <section class="BOX-4">
        <h2>4. Integral – Costo Acumulado</h2>

        <p>Para calcular el costo acumulado durante T años se integra:</p>

        <div class="formula">{expresionA}</div>

        <p>Solución exacta:</p>

        <div class="formula">{expresionB}</div>

        <!-- NUEVA DESCRIPCIÓN -->
        <p>
          La integral se emplea para calcular el costo total acumulado durante
          un periodo de tiempo. Matemáticamente, corresponde al área bajo la
          curva C(t). Este valor es crucial para estimar gastos totales,
          planificar presupuestos, evaluar amortizaciones y determinar el
          impacto económico del deterioro del servidor.
        </p>

        <div class="grid-2">
          <div>
            <h3>Gráfico de la integral acumulada</h3>    <!-- BORRAR CUANDO SE implemente el grafico -->
            <div class="area-placeholder">[Gráfico S(T)]</div>
          </div>
          <div>
            <h3>Área bajo la curva C(t)</h3>             <!-- BORRAR CUANDO SE implemente el grafico -->
            <div class="area-placeholder">[Área bajo C(t)]</div>
          </div>
        </div>
      </section>'''

def SectionBOX6():
   return '''
      <section class="BOX-5">
        <h2>5. Tabla de Valores</h2>

        <!-- NUEVA DESCRIPCIÓN -->
        <p>
          Los valores mostrados se obtienen mediante cálculos apoyados en
          herramientas de simulación. La tabla permite comparar directamente el
          valor de la función, su derivada y el costo acumulado, facilitando el
          análisis del comportamiento del sistema en distintos momentos del
          tiempo.
        </p>
        <!-- BORRAR CUANDO SE implemente LA tabla -->
        <table>
          <thead>
            <tr>
              <th>t (años)</th>
              <th>C(t)</th>
              <th>C'(t)</th>
              <th>Costo acumulado</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>0</td>
              <td>10</td>
              <td>5</td>
              <td>0</td>
            </tr>
            <tr>
              <td>1</td>
              <td>17</td>
              <td>9</td>
              <td>158</td>
            </tr>
            <tr>
              <td>2</td>
              <td>28</td>
              <td>13</td>
              <td>536</td>
            </tr>
            <tr>
              <td>3</td>
              <td>43</td>
              <td>17</td>
              <td>1218</td>
            </tr>
            <tr>
              <td>4</td>
              <td>62</td>
              <td>21</td>
              <td>2224</td>
            </tr>
            <tr>
              <td>5</td>
              <td>85</td>
              <td>25</td>
              <td>3620</td>
            </tr>
          </tbody>
        </table>
      </section>
'''
def SectionBOX7():
   return '''
      <section class="BOX-6">
        <h2>6. Interpretación Automática</h2>
        <p>
          • La derivada muestra que el servidor empeora más rápido cada año.
          <br />• La integral indica que el costo acumulado se dispara a partir
          del año 4. <br />• Se recomienda reemplazar el hardware entre los años
          4 y 5.
        </p>
        <!-- NUEVA DESCRIPCIÓN -->
        <p>
          En esta última sección, los resultados matemáticos se traducen a un
          contexto práctico. Se interpreta el significado de la tasa de
          variación del costo, la acumulación de gastos y los momentos críticos
          en que se vuelve conveniente reemplazar el hardware. Estas
          conclusiones permiten tomar decisiones informadas basadas en el
          comportamiento real del sistema.
        </p>
      </section>
    </main>
'''

def SectionBOX0():
   return '''
   <p style='text-align:center; color:gray;'>
    MAT1188 – Colaboradores
   </p>
  '''