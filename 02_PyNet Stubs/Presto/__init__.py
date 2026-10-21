# Auto-generated — Presto 26.01 — PrestoLib (presto.tlb)

"""
RIB Presto API (COM, ProgID "Presto.App.18") -- reference stubs for PyNET for Presto.

Scripts never import this module: the host injects the application as __presto__, a late-bound
proxy, and calls each member by name. Every member below is called like a method, properties
included:

    app = __presto__
    app.Project()                                   # path of the active obra
    app.FindEqual("Conceptos", "Conceptos.Nat", 0)  # 0 = found

Proxy extras (not in the type library): app._get(name, *index) forces a property read,
app._set(name, value) a property write, app._com.Target is the raw System.__ComObject.

Return-code convention: Find*/GetElement/Open... return 0 on success. Read numeric fields with
GetFieldNum / GetField (GetFieldStr returns None for them). See docs/presto.md and
.claude/commands/PrestoApiPatterns.md for what has been verified.
"""

class PrestoApplication:
    """COM: PrestoLib.com_presto -- Application object for the Presto application"""
    def __init__(self, *args) -> None: ...
    def AddCert(self, bstrCertDescription: str = ..., nCertColor: int = ...) -> int:
        """Añade una nueva certificación a continuación de la última. Devuelve 0 en caso de error y el número de la certificación añadida en caso contrario"""
    def AddSpace(self, bstrSpcCode: str = ..., bstrSpcDescription: str = ..., nSpcColor: int = ..., dBIMLevel: float = ...) -> int:
        """Añade un nuevo espacio a continuación del último. Devuelve 0 en caso de error y el número del espacio añadido en caso contrario"""
    def BeginRedo(self, ) -> int:
        """Inicio de acciones que se pueden deshacer. Devuelve 0: correcto"""
    def Calculate(self, nCalculationMode: int) -> None:
        """Lanza un cálculo. nCalculationMode 1: Todo 2: Precios 3: Mediciones 4: Tiempos 5: Documentos 6: Costes reales"""
    def CheckProject(self, ) -> None:
        """Comprueba el proyecto"""
    def Close(self, ) -> None:
        """Cierra una obra de Presto."""
    def CloseWindow(self, nCloseWindowId: int) -> None:
        """Cierra la ventana principal indicada 0: Árbol 1: Presupuesto 2: Mediciones 3: Mediciones temporales 4: Espacios"""
    def Command(self, opcion: str) -> None:
        """Ejecuta una opcion"""
    def Copy(self, origen: str, destino: str, dimension1: int = ..., dimension2: int = ...) -> None:
        """Copia un campo en otro"""
    def CreateSpace(self, nSpcNumber: int, bstrSpcCode: str = ..., bstrSpcDescription: str = ..., nSpcColor: int = ..., dBIMLevel: float = ...) -> int:
        """Crea un espacio. Añade los espacios necesarios hasta nSpcNumber. Devuelve distinto de 0 en caso de error"""
    def CreateVariable(self, bstrVarGuid: str, bstrVarName: str, bstrVarDescription: str = ..., nVarSource: int = ..., nVarType: int = ..., nVarCalcType: int = ..., dVarMinVal: float = ..., dVarStepVal: float = ..., dVarMaxVal: float = ..., nVarIsCombo: int = ..., bstrVarComboList: str = ..., nVarStatus: int = ..., nVarIsReadOnly: int = ..., nRevitParam_Shared: int = ..., bstrUnitType: str = ..., bstrUnit: str = ..., bstrRevitParam_StorageType: str = ..., bstrRevitParam_Type: str = ..., bstrGroup: str = ..., bstrRevitParam_SharedGuid: str = ..., nVarDec: int = ..., bstrVarExp: str = ..., bstrVarCond: str = ..., nVarColor: int = ...) -> str:
        """Crea una variable nueva o actualiza la existente. Devuelve el GUID de la variable creada/actualizada o GUID vacío si no pudo"""
    def Delete(self, obra: str) -> int:
        """Borra una obra de Presto. Devuelve 0: correcto"""
    def DeleteRecord(self, tabla: str, todo: int = ...) -> int:
        """Borra un registro. todo 1: Borra los registros relacionados. Devuelve 0: correcto"""
    def Duplicate(self, codigo: str, nuevo: str) -> int:
        """Duplica un registro. Devuelve 0: correcto"""
    def EndRedo(self, ) -> None:
        """Fin de acciones que se pueden deshacer"""
    def EvalNum(self, expresion: str) -> float:
        """Evalua una expresion de Presto."""
    def EvalStr(self, expresion: str) -> str:
        """Evalua una expresion de Presto"""
    def Exit(self, ) -> None:
        """Cierra la ventana principal"""
    def ExportFIEBDC(self, archivo: str) -> int:
        """Exporta la obra en formato FIEBDC"""
    def ExportRPT(self, informe: str, archivo: str, parametros: int = ..., formato: int = ..., rellenar_blancos: int = ..., imprimir_cabecera: int = ..., separador_campos: int = ..., imprimir: int = ..., pagina_inicial: int = ..., pagina_final: int = ..., columnas: int = ..., lineas: int = ..., anadir: int = ...) -> int:
        """Exporta un informe informe: archivo .rpt, archivo: archivo destino, parametros 0: defecto 1: preguntar, formato 0: ASCII 1: RTF, rellenar_blancos 0: Si 1: No, imprimir_cabecera 0: Nunca 1: primera página 2: siempre"""
    def FindEqual(self, tabla: str, clave: str, valor: object) -> int:
        """Busca igual. Devuelve 0: correcto"""
    def FindFirst(self, tabla: str, clave: str = ...) -> int:
        """Posicionar en el primer registro. Campo clave obligatorio. Devuelve 0: correcto"""
    def FindGreat(self, tabla: str, clave: str, valor: object) -> int:
        """Busca mayor. Devuelve 0: correcto"""
    def FindGreatEqual(self, tabla: str, clave: str, valor: object) -> int:
        """Busca mayor o igual. Devuelve 0: correcto"""
    def FindLast(self, tabla: str, clave: str = ...) -> int:
        """Posicionar en el ultimo registro. Campo clave obligatorio. Devuelve 0: correcto"""
    def FindLessEqual(self, tabla: str, clave: str, valor: object) -> int:
        """Busca menor o igual. Devuelve 0: correcto"""
    def FindNext(self, tabla: str, clave: str = ...) -> int:
        """Posicionar en el registro siguiente. Campo clave obligatorio. Devuelve 0: correcto"""
    def FindPos(self, tabla: str, clave: str, pos: int) -> int:
        """Se posiciona en un registro por la posicion. Devuelve 0: correcto"""
    def FindPrev(self, tabla: str, clave: str = ...) -> int:
        """Posicionar en el registro anterior. Campo clave obligatorio. Devuelve 0: correcto"""
    def GetElement(self, elemento: int, anida: int = ...) -> int:
        """Recupera un elemento"""
    def GetField(self, campo: str, dimension: int = ...) -> object:
        """Devuelve el valor de un campo"""
    def GetFieldBinary(self, campo: str) -> object:
        """Devuelve el valor de un campo binario"""
    def GetFieldNum(self, campo: str, dimension: int = ...) -> float:
        """Devuelve el valor de un campo numérico"""
    def GetFieldStr(self, campo: str, dimension: int = ...) -> str:
        """Devuelve el valor de un campo cadena"""
    def GetPos(self, tabla: str) -> int:
        """Devuelve la posicion de un registro"""
    def GetSelection(self, first: int, tabla: str) -> int:
        """Devuelve la seleccion actual"""
    def GetText(self, campo: str, tipo: int = ...) -> str:
        """Devuelve el texto de un registro, tipo 1: Txt 2: RTF"""
    def ImportCad(self, proyecto: str, archivo: str, tipo: int) -> int:
        """Importa un archivo de PrestoCad, tipo 0: Fiebdc 1: Archicad. Devuelve 0: correcto"""
    def ImportFIEBDC(self, archivo: str) -> int:
        """Importa la obra en formato FIEBDC"""
    def InfoCode(self, proyecto: str, codigo: str, unidad: str, resumen: str, precio: str) -> int:
        """Informacion de un concepto de Presto. Devuelve 0: correcto; has [out] parameters"""
    def InitRecord(self, tabla: str) -> int:
        """Inicia un registro"""
    def InitVar(self, ) -> None:
        """Suprime las variables declaradas"""
    def InsertAttachment(self, bstrTableName: str, bstrCode: str, bstrDescription: str, bstrExtension: str, vrBuffer: object, nType: int = ..., bResetSourcePath: int = ...) -> str:
        """Inserta un archivo asociado a partir de un buffer. Devuelve el guid del archivo"""
    def InsertAttachmentFromPath(self, bstrTableName: str, bstrCode: str, bstrFilePath: str, bResetSourcePath: int = ...) -> str:
        """Inserta un archivo asociado a partir de una ruta. Devuelve el guid del archivo"""
    def InsertRecord(self, tabla: str) -> int:
        """Inserta un registro. Devuelve 0: correcto"""
    def IULanguage(self, ) -> int:
        """IULanguage 0: castellano 1: catalán 2: inglés 3: francés 4: gallego 5: portugués 6: alemán; property (read)"""
    def LogBegin(self, bstrLogHead: str) -> int:
        """Inicia el sistema de log de Presto. bstrLogHead es el mensaje que mostrará la primera línea del log. Devuelve 0: correcto 1: incorrecto"""
    def LogEnd(self, ) -> int:
        """Cierra el sistema de log y muestra la ventana. Devuelve 0: correcto 1: incorrecto"""
    def LogMsg(self, bstrMessage: str, nMode: int) -> int:
        """Agrega un mensaje al sistema de log de Presto. nMode 0: info 1: warning 2: error. Devuelve 0: correcto 1: incorrecto"""
    def MsgClear(self, ) -> int:
        """Borra la ventana de mensajes"""
    def MsgSetTabs(self, bstrMessage: str) -> int:
        """Pone los tabuladores en la ventana de mensajes carro. bstrMessage: . Devuelve 0: correcto 1: incorrecto"""
    def MsgText(self, bstrMessage: str, nMode: int) -> int:
        """Muestra un texto en la ventana de mensajes sin añadir un retorno de carro. nMode 0: info 1: warning 2: error. Devuelve 0: correcto 1: incorrecto"""
    def MsgWrapText(self, nMode: int) -> int:
        """Pone ajuste de línea en la ventana de mensajes. nMode 0: nMode 1:. Devuelve 0: correcto 1: incorrecto"""
    def New(self, obra: str) -> int:
        """Crea y abre una obra de Presto. Devuelve 0: correcto"""
    def Open(self, bstrPath: str, nMode: int = ...) -> int:
        """Abre una obra existente. nMode 0: lectura/escritura 1: sólo lectura 2: convierte a formato .Presto. Devuelve 0: correcto, Otro valor: error"""
    def PrintRPT(self, informe: str, parametros: int = ..., copias: int = ..., impresora: int = ...) -> int:
        """Imprime un informe, hwnd: handle de la ventana, informe: archivo .rpt, parametros 0: defecto 1: preguntar, copias n§ copias, impresora 0: defecto 1: pregunta"""
    def Project(self, ) -> str:
        """Proyecto de Presto; property (read)"""
    def ProjectLanguage(self, ) -> int:
        """ProjectLanguage 0: castellano 1: catalán 2: inglés 3: francés 4: gallego 5: portugués 6: alemán; property (read)"""
    def Quit(self, ) -> None:
        """Cierra la aplicacion Presto activa."""
    def ReadOnly(self, ) -> int:
        """Obra en solo lectura; property (read)"""
    def ReadTableByKey(self, nOutputFormat: int, bstrTableName: str, bstrTableKeyName: str, bstrTableFieldsToRead: str, bstrTableOrderFieldName: str = ..., bOrderDescending: int = ...) -> str:
        """Recorre un tabla de la BD por un campo clave accediendo a los valores de los campos indicados. nOutputFormat 0: Json plano 1: Json formateado 2: Texto plano"""
    def ReadTableByKeyValue(self, nOutputFormat: int, bstrTableName: str, bstrTableKeyName: str, vTableKeyValue: object, bstrTableFieldsToRead: str, bstrTableOrderFieldName: str = ..., bOrderDescending: int = ...) -> str:
        """Recorre un tabla de la BD para un valor de un campo clave accediendo a los valores de los campos indicados. nOutputFormat 0: Json plano 1: Json formateado 2: Texto plano"""
    def Recalculate(self, activar: int) -> None:
        """Bloquea o Desbloquea los recalculos"""
    def Rename(self, campo: str, valor: str) -> int:
        """Renombra un registro. Devuelve 0: correcto"""
    def SelCode(self, HWND: int, proyecto: str, relacion: str) -> int:
        """Elige un concepto de Presto. Devuelve 0: Codigo en blanco 1: Codigo seleccionado -1: Cancelar Otros: error; has [out] parameters"""
    def SetCharacter(self, modo: int) -> None:
        """Selecciona juego de caracteres, modo 0: ANSI 1: OEM"""
    def SetConceptVarValue(self, bstrVarGuid: str, bstrConceptCode: str, vVarValue: object, nValueType: int = ..., bstrValueUserTxt: str = ..., dValueUserNum: float = ..., bstrRevitParam_ElementId: str = ..., nOnlyNew: int = ...) -> int:
        """Asigna valor a una variable en un concepto. Devuelve distinto de 0 en caso de error"""
    def SetCurrentInvPeriod(self, sDate: str) -> int:
        """Establece como certificación actual aprobada la fecha recibida en formato (yyyymmdd). Devuelve 0:correcto 1:incorrecto"""
    def SetElement(self, elemento: int, tabla: str, clave: str = ..., mascara: str = ..., seleccion: str = ..., ordenar_por: str = ..., orden: int = ...) -> int:
        """Define un elemento"""
    def SetField(self, campo: str, valor: object, dimension: int = ...) -> None:
        """Modifica un campo"""
    def SetFieldBinary(self, campo: str, valor: object) -> None:
        """Modifica un campo binario"""
    def SetModal(self, activar: int) -> None:
        """Bloquea o Desbloquea el uso de Presto, activar 0: desactiva 1: activa"""
    def SetPriceVarValue(self, bstrVarGuid: str, bstrPriceSupCode: str, bstrPriceInfCode: str, vVarValue: object, nValueType: int = ..., bstrValueUserTxt: str = ..., dValueUserNum: float = ..., bstrRevitParam_ElementId: str = ..., nOnlyNew: int = ...) -> int:
        """Asigna valor a una variable en un precio. Devuelve distinto de 0 en caso de error"""
    def SetRelationVarValue(self, bstrVarGuid: str, bstrRelSupCode: str, bstrRelInfCode: str, vVarValue: object, nValueType: int = ..., bstrValueUserTxt: str = ..., dValueUserNum: float = ..., bstrRevitParam_ElementId: str = ..., nOnlyNew: int = ...) -> int:
        """Asigna valor a una variable en una relación. Devuelve distinto de 0 en caso de error"""
    def SetTakeoffInsertMode(self, nTakeoffInsertMode: int) -> None:
        """Establece el modo de inserción de mediciones 0: en Mediciones 1: en MedicionesTmp si falla en Mediciones 2: en MedicionesTmp 3: en MedicionesTmp con borrado previo"""
    def SetTakeoffVarValue(self, bstrVarGuid: str, bstrTakeoffGuidElem: str, bstrTakeoffGuidAux: str, vVarValue: object, nValueType: int = ..., bstrValueUserTxt: str = ..., dValueUserNum: float = ..., bstrRevitParam_ElementId: str = ..., nOnlyNew: int = ...) -> int:
        """Asigna valor a una variable en una línea de medición. Devuelve distinto de 0 en caso de error"""
    def SetText(self, campo: str, valor: str) -> None:
        """Modifica el texto de un registro"""
    def SetUniqueVarValue(self, bstrVarGuid: str, vVarValue: object) -> int:
        """Asigna valor a una variable de asignación única. La variable debe existir. Devuelve distinto de 0 en caso de error"""
    def SetUpdateScreen(self, activar: int) -> None:
        """Bloquea o Desbloquea la visualizacion de cambios"""
    def SetVar(self, variable: str, valor: str) -> None:
        """Modifica una variable"""
    def ShowWindow(self, nShowWindowId: int) -> None:
        """Abre y pone como activa la ventana principal indicada 0: Árbol 1: Presupuesto 2: Mediciones 3: Mediciones temporales 4: Espacios"""
    def SQLServerDelete(self, bstrServer: str, bstrUser: str, bstrPassword: str, nPort: int, nTimeout: int, bstrDataBase: str, bstrGuid: str) -> int:
        """Borra en SQL Server"""
    def SQLServerExport(self, bstrServer: str, bstrUser: str, bstrPassword: str, nPort: int, nTimeout: int, bstrDataBase: str, bOwerWrite: int, bCalcFields: int, bstrSelTables: str) -> int:
        """Exporta a SQL Server"""
    def SQLServerImport(self, bstrServer: str, bstrUser: str, bstrPassword: str, nPort: int, nTimeout: int, bstrDataBase: str, bstrGuid: str, bstrSelTables: str) -> int:
        """Importa desde SQL Server"""
    def Status(self, ) -> int:
        """Status; property (read)"""
    def SubVersionNum(self, ) -> int:
        """Sub-versión de Presto en formato número; property (read)"""
    def UpdateRecord(self, tabla: str) -> int:
        """Modifica un registro. Devuelve 0: correcto"""
    def UpdateScreen(self, ) -> None:
        """Actualiza las ventanas"""
    def VersionNum(self, ) -> int:
        """Versión de Presto en formato número; property (read)"""
    def VersionStr(self, ) -> str:
        """Nombre completo de la versión de Presto; property (read)"""
