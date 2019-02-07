import re
html = """<!DOCTYPE html>
<html>
   <head>
      <title>Resultado da Execução</title>
      <meta charset="UTF-8">
      <style>
table {
  border-collapse: collapse;
  width: 100%;
}

th, td {
  text-align: left;
  padding: 8px;
}

tr:nth-child(even){background-color: #f2f2f2}

th {
  background-color: #4CAF50;
  color: white;
}
</style>
   </head>
   <body>
      <table class="table table-striped">
         <thead>
            <tr>
               <th>Name</th>
               <th> NEXT_DATE</th>
               <th>INVERVAL</th>
               <th> FAILURES</th>
               <th> BROKEN</th>
               <th> LAST_REFRESH</th>
               <th> LAST_REFRESH_TYPE</th>
            </tr>
         </thead>
         <tbody>
            <tr>
               <td>AREA_RISCO.AREA_RISCO_GEOTECNICO</td>
               <td>21:40 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (2400/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:54 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>AREA_RISCO.LOTE_CTM_ARG</td>
               <td>21:26 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (1590/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:40 31:01:2019</td>
               <td>COMPLETE</td>
            </tr>
            <tr>
               <td>AREA_RISCO.LOTE_CTM_ARG</td>
               <td>21:26 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (1590/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:40 31:01:2019</td>
               <td>COMPLETE</td>
            </tr>
            <tr>
               <td>AREA_RISCO.TIPO_AREA_RISCO_GEOTECNICO</td>
               <td>21:27 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (1620/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:41 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>CADASTRO_TECNICO.BAIRRO_OFICIAL</td>
               <td>21:40 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (2430/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:54 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>CADASTRO_TECNICO.BAIRRO_POPULAR</td>
               <td>21:43 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (2580/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:57 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>CADASTRO_TECNICO.ENDERECO_PBH</td>
               <td>21:42 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (2520/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:56 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>CADASTRO_TECNICO.FONTE_INFORMACAO</td>
               <td>21:14 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (870/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:28 31:01:2019</td>
               <td>COMPLETE</td>
            </tr>
            <tr>
               <td>CADASTRO_TECNICO.LIMITE_MUNICIPIO</td>
               <td>00:00 01:01:4000</td>
               <td>TRUNC(SYSDATE) + 21/24 + (750/24/60/60)</td>
               <td></td>
               <td>Y</td>
               <td>00:04 09:06:2017</td>
               <td>COMPLETE</td>
            </tr>
            <tr>
               <td>CADASTRO_TECNICO.LOTE_CTM</td>
               <td>21:41 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (2490/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:55 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>CADASTRO_TECNICO.QUADRA_CTM</td>
               <td>21:41 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (2460/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:55 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>CADASTRO_TECNICO.REGIONAL</td>
               <td>00:00 01:01:4000</td>
               <td>TRUNC(SYSDATE) + 21/24 + (900/24/60/60)</td>
               <td></td>
               <td>Y</td>
               <td>00:08 09:06:2017</td>
               <td>COMPLETE</td>
            </tr>
            <tr>
               <td>CADASTRO_TECNICO.SETOR_CTM</td>
               <td>21:14 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (840/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:28 31:01:2019</td>
               <td>COMPLETE</td>
            </tr>
            <tr>
               <td>CADASTRO_TECNICO.TESTADA_LOTE_CTM</td>
               <td>21:42 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (2550/24/60/60) </td>
               <td>0</td>
               <td>N</td>
               <td>01:56 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>CADASTRO_TECNICO.TIPO_BAIRRO</td>
               <td>21:13 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (810/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:27 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>CADASTRO_TECNICO.TIPO_DESTINACAO</td>
               <td>21:13 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (780/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:27 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>CP.AREA_ORIGEM_PLANTA_CP</td>
               <td>21:44 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (2640/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:58 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>CP.AREA_REMANESCENTE_LOTE_CP</td>
               <td>21:30 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (1800/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:44 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>CP.AREA_REMANESCENTE_PLANTA_CP</td>
               <td>21:29 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (1770/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:43 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>CP.ARTICUL_JK_1942</td>
               <td>21:29 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (1740/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:43 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>CP.COMPATIBILIZACAO</td>
               <td>21:21 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (1290/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:35 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>CP.CORRESPONDENCIA_PL</td>
               <td>21:21 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (1260/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:35 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>CP.DESAPROPRIACAO</td>
               <td>21:20 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (1230/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:34 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>CP.DESTINACAO_LOTE_CP</td>
               <td>21:26 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (1560/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:40 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>CP.DIVISAS_LOTE_CP</td>
               <td>21:30 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (1830/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:44 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>CP.LOTE_CP</td>
               <td>21:27 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (1650/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:41 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>CP.LOTE_CP_INF_COMPLEMENTAR</td>
               <td>21:17 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (1050/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:31 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>CP.MATRICULA_PLANTA_CP</td>
               <td>21:17 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (1020/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:31 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>CP.MOTIVO_CP_CANCELADO</td>
               <td>21:25 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (1530/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:39 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>CP.MUDANCA_DENOMINACAO</td>
               <td>21:20 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (1200/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:34 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>CP.ORIGEM_LOTE_CP</td>
               <td>21:19 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (1170/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:33 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>CP.ORIGEM_LOTE_CP_HISTORICO</td>
               <td>21:19 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (1140/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:33 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>CP.ORIGEM_PLANTA_CP</td>
               <td>21:18 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (1110/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:32 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>CP.ORIGEM_PLANTACP_HISTORICO</td>
               <td>21:18 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (1080/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:32 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>CP.PLANTA_CP</td>
               <td>21:31 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (1860/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:45 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>CP.PROJETO_PARCELAMENTO_CP</td>
               <td>21:44 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (2670/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:58 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>CP.TESTADA_LOTE_CP</td>
               <td>21:28 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (1680/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:42 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>CP.TIPO_APROVACAO_PLANTA_CP</td>
               <td>21:25 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (1500/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:39 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>CP.TIPO_DESCOMISSIONADO</td>
               <td>21:23 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (1380/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:37 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>CP.TIPO_INF_COMPLEMENTAR</td>
               <td>21:24 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (1470/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:38 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>CP.TIPO_NAO_COMPATIBILIZACAO</td>
               <td>21:22 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (1350/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:36 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>CP.TIPO_ORIGEM_PLANTA_CP</td>
               <td>21:24 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (1440/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:38 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>CP.TIPO_SITUACAO_LOTE</td>
               <td>21:23 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (1410/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:37 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>CP.TIPO_VINCULACAO_USO</td>
               <td>21:22 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (1320/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:36 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>DIPC.ALTIMETRIA_DIR_PROTECAO</td>
               <td>21:11 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (690/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:25 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>DIPC.AREA_PROTECAO_CULTURAL</td>
               <td>21:34 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (2070/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:48 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>DIPC.BEM_CULTURAL_IMOVEL</td>
               <td>21:12 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (720/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:26 31:01:2019</td>
               <td>COMPLETE</td>
            </tr>
            <tr>
               <td>DIPC.BEM_CULTURAL_INTEGRADO</td>
               <td>21:33 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (1980/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:47 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>DIPC.BEM_CULTURAL_MOVEL</td>
               <td>21:32 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (1950/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:46 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>DIPC.BEM_CULTURAL_NATURAL</td>
               <td>21:34 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (2040/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:48 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>DIPC.BEM_CULTURAL_URBANISTICO</td>
               <td>21:32 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (1920/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:46 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>DIPC.DIRETRIZ_PROTECAO</td>
               <td>00:00 01:01:4000</td>
               <td>TRUNC(SYSDATE) + 21/24 + (2010/24/60/60)</td>
               <td></td>
               <td>Y</td>
               <td>01:47 27:02:2018</td>
               <td>COMPLETE</td>
            </tr>
            <tr>
               <td>DIPC.TIPO_AREA_PROTECAO</td>
               <td>21:10 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (630/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:24 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>DIPC.TIPO_GRAU_PROTECAO</td>
               <td>21:11 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (660/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:25 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>IMAGEM_BH.ARTICUL2</td>
               <td>00:00 01:01:4000</td>
               <td>TRUNC(SYSDATE) + 1 + (1740/24/60/60) </td>
               <td></td>
               <td>N</td>
               <td>11:58 13:06:2017</td>
               <td>COMPLETE</td>
            </tr>
            <tr>
               <td>IMAGEM_BH.ARTICUL5</td>
               <td>00:00 01:01:4000</td>
               <td>TRUNC(SYSDATE) + 1 + (1770/24/60/60) </td>
               <td></td>
               <td>N</td>
               <td>11:27 13:06:2017</td>
               <td>COMPLETE</td>
            </tr>
            <tr>
               <td>MEIO_AMBIENTE.AREA_PRESERVACAO_PERMANENTE</td>
               <td>21:49 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (2970/24/60/60) </td>
               <td>0</td>
               <td>N</td>
               <td>02:03 31:01:2019</td>
               <td>COMPLETE</td>
            </tr>
            <tr>
               <td>MEIO_AMBIENTE.LOTE_CTM_APP</td>
               <td>21:16 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (960/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:30 31:01:2019</td>
               <td>COMPLETE</td>
            </tr>
            <tr>
               <td>MEIO_AMBIENTE.LOTE_CTM_APP</td>
               <td>21:16 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (960/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:30 31:01:2019</td>
               <td>COMPLETE</td>
            </tr>
            <tr>
               <td>MEIO_AMBIENTE.LOTE_CTM_UCA</td>
               <td>21:15 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (930/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:29 31:01:2019</td>
               <td>COMPLETE</td>
            </tr>
            <tr>
               <td>MEIO_AMBIENTE.TIPO_AREA_PRESERV_PERMA</td>
               <td>00:49 01:02:2019</td>
               <td>TRUNC(SYSDATE) + 1 + (2970/24/60/60) </td>
               <td>0</td>
               <td>N</td>
               <td>00:49 31:01:2019</td>
               <td>COMPLETE</td>
            </tr>
            <tr>
               <td>MEIO_AMBIENTE.TIPO_UNID_CONSERV_AMBIENTAL</td>
               <td>21:16 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (990/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:30 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>MEIO_AMBIENTE.UNID_CONSERV_AMBIENTAL</td>
               <td>21:35 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (2100/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:49 31:01:2019</td>
               <td>COMPLETE</td>
            </tr>
            <tr>
               <td>PARAM_URB.ADE</td>
               <td>21:39 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (2370/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:53 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>PARAM_URB.AEIS</td>
               <td>21:39 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (2340/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:53 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>PARAM_URB.AREA_LINDEIRA_OPERACAO_URB</td>
               <td>21:38 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (2280/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:52 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>PARAM_URB.AREA_OPERACAO_URB</td>
               <td>21:37 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (2250/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:51 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>PARAM_URB.AREA_PROTECAO_URB</td>
               <td>21:37 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (2220/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:51 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>PARAM_URB.CLASSIF_VIARIA_PERMISSIVIDADE</td>
               <td>21:07 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (420/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:21 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>PARAM_URB.CLASS_LARGURA_VIA</td>
               <td>21:07 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (450/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:21 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>PARAM_URB.LOTE_CTM_ADE</td>
               <td>21:10 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (600/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:24 31:01:2019</td>
               <td>COMPLETE</td>
            </tr>
            <tr>
               <td>PARAM_URB.LOTE_CTM_AEIS</td>
               <td>21:09 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (540/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:23 31:01:2019</td>
               <td>COMPLETE</td>
            </tr>
            <tr>
               <td>PARAM_URB.LOTE_CTM_AREA_OPERACAO_URB</td>
               <td>21:06 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (390/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:20 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>PARAM_URB.LOTE_CTM_AREA_PROTECAO_URB</td>
               <td>21:09 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (570/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:23 31:01:2019</td>
               <td>COMPLETE</td>
            </tr>
            <tr>
               <td>PARAM_URB.LOTE_CTM_PROJ_VIARIO_PRIOR</td>
               <td>21:08 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (510/24/60/60)  </td>
               <td>0</td>
               <td>N</td>
               <td>01:22 31:01:2019</td>
               <td>COMPLETE</td>
            </tr>
            <tr>
               <td>PARAM_URB.LOTE_CTM_ZONEAMENTO</td>
               <td>21:06 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (360/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:20 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>PARAM_URB.OPERACAO_URBANA</td>
               <td>21:05 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (330/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:19 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>PARAM_URB.PERMISSIVIDADE_REGRA_ESPEC</td>
               <td>21:05 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (300/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:19 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>PARAM_URB.PROJ_VIARIO_PRIOR</td>
               <td>21:36 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (2190/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:50 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>PARAM_URB.SUBDIVISAO_OPERACAO_URB</td>
               <td>21:04 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (270/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:18 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>PARAM_URB.TIPO_ADE</td>
               <td>21:04 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (240/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:18 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>PARAM_URB.TIPO_AEIS</td>
               <td>21:03 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (210/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:17 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>PARAM_URB.TIPO_AREA_PROTECAO_URB</td>
               <td>00:00 01:01:4000</td>
               <td>TRUNC(SYSDATE) + 21/24 + (180/24/60/60)</td>
               <td></td>
               <td>Y</td>
               <td>01:17 27:02:2018</td>
               <td>COMPLETE</td>
            </tr>
            <tr>
               <td>PARAM_URB.TIPO_CLASSIFICACAO_VIARIA</td>
               <td>21:02 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (150/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:16 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>PARAM_URB.TIPO_OPERACAO_URB</td>
               <td>21:02 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (120/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:16 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>PARAM_URB.TIPO_PERMISSIVIDADE</td>
               <td>21:01 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (90/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:15 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>PARAM_URB.TIPO_ZONA_PROT_AERONAUTICA</td>
               <td>21:01 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (60/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:15 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>PARAM_URB.TIPO_ZONA_RUIDO_AERONAUTICA</td>
               <td>21:00 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (30/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:14 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>PARAM_URB.TIPO_ZONEAMENTO</td>
               <td>21:00 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (0/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:14 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>PARAM_URB.ZONA_PROT_AERONAUTICA</td>
               <td>21:36 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (2160/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:50 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>PARAM_URB.ZONA_RUIDO_AERONAUTICA</td>
               <td>21:35 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (2130/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:49 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>PARAM_URB.ZONEAMENTO</td>
               <td>21:38 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (2310/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:52 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>PARAM_URB.ZONEAMENTO_QUADRA_CTM</td>
               <td>21:08 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (480/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:22 31:01:2019</td>
               <td>COMPLETE</td>
            </tr>
            <tr>
               <td>PLANEJ.TERRITORIO_GESTAO_COMPART</td>
               <td>21:31 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (1890/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:45 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>SISTEMA_VIARIO.CLASS_LOGRADOURO</td>
               <td>21:48 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (2910/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>02:02 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>SISTEMA_VIARIO.CLASS_NOME_LOGRADOURO</td>
               <td>21:48 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (2880/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>02:02 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>SISTEMA_VIARIO.LOGRADOURO</td>
               <td>21:47 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (2850/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>02:01 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>SISTEMA_VIARIO.LOGRADOURO_ATRIBUTOS</td>
               <td>21:47 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (2820/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>02:01 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>SISTEMA_VIARIO.LOGRADOURO_CEP</td>
               <td>21:45 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (2700/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:59 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>SISTEMA_VIARIO.LOGRADOURO_OUTROS_NOMES</td>
               <td>21:49 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (2940/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>02:03 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>SISTEMA_VIARIO.TIPO_DIVISA</td>
               <td>21:46 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (2790/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>02:00 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>SISTEMA_VIARIO.TIPO_DOCTO_ORIGEM</td>
               <td>21:46 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (2760/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>02:00 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>SISTEMA_VIARIO.TIPO_LOGRADOURO</td>
               <td>21:45 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (2730/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:59 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>SISTEMA_VIARIO.TRECHO</td>
               <td>21:43 31:01:2019</td>
               <td>TRUNC(SYSDATE) + 21/24 + (2610/24/60/60)</td>
               <td>0</td>
               <td>N</td>
               <td>01:57 31:01:2019</td>
               <td>FAST</td>
            </tr>
            <tr>
               <td>SIURBE.IMOVEL2</td>
               <td>00:00 01:02:2019</td>
               <td>TRUNC(SYSDATE) + 0/24 + 1  </td>
               <td>0</td>
               <td>N</td>
               <td>00:00 31:01:2019</td>
               <td>COMPLETE</td>
            </tr>
            <tr>
               <td>SIURBE.LOTE_CTM_ATRIBUTOS2</td>
               <td>00:00 01:02:2019</td>
               <td>TRUNC(SYSDATE) + 0/24 + 1  </td>
               <td>0</td>
               <td>N</td>
               <td>00:00 31:01:2019</td>
               <td>COMPLETE</td>
            </tr>
         </tbody>
      </table>
   </body>
</html>
"""
	
#print (html)

m = re.search('<tr>((.|\n)*?)<\/tr>', html)
##m.group(0)
print(m.group(0))