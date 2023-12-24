class Heu:

    def __init__(self):
        self.heuristicas = list()
    
    def fillHeuristicas(self):
        heuristicasBraga= {
            "Amares":15,
            "Barcelos":24,
            "Braga":1,
            "Cabeceiras de Basto":37,
            "Celorico de Basto":41,
            "Esposende":31,
            "Fafe":29,
            "Guimarães":20,
            "Póvoa de Lanhoso":14, 
            "Terras de Bouro":34,
            "Vieira do Minho":28, 
            "Vila Nova de Famalicão":23, 
            "Vila Verde":13,
            "Vizela":28
        }

        heuristicasAmares= {
            "Amares":1,
            "Barcelos":31,
            "Braga":15,
            "Cabeceiras de Basto":29,
            "Celorico de Basto":34,
            "Esposende":40,
            "Fafe":26,
            "Guimarães":28,
            "Póvoa de Lanhoso":11, 
            "Terras de Bouro":13,
            "Vieira do Minho":21, 
            "Vila Nova de Famalicão":32, 
            "Vila Verde":9,
            "Vizela":32
        }

        heuristicasBarcelos= {
            "Amares":31,
            "Barcelos":1,
            "Braga":24,
            "Cabeceiras de Basto":60,
            "Celorico de Basto":63,
            "Esposende":13,
            "Fafe":50,
            "Guimarães":32,
            "Póvoa de Lanhoso":33, 
            "Terras de Bouro":44,
            "Vieira do Minho":51, 
            "Vila Nova de Famalicão":26, 
            "Vila Verde":25,
            "Vizela":37
        }
        heuristicasCabeceiras= {
            "Amares":29,
            "Barcelos":60,
            "Braga":37,
            "Cabeceiras de Basto":1,
            "Celorico de Basto":22,
            "Esposende":60,
            "Fafe":26,
            "Guimarães":33,
            "Póvoa de Lanhoso":25, 
            "Terras de Bouro":40,
            "Vieira do Minho":18, 
            "Vila Nova de Famalicão":57, 
            "Vila Verde":40,
            "Vizela":38
        }
        heuristicasCelorico= {
            "Amares":34,
            "Barcelos":63,
            "Braga":41,
            "Cabeceiras de Basto":22,
            "Celorico de Basto":1,
            "Esposende":80,
            "Fafe":19,
            "Guimarães":28,
            "Póvoa de Lanhoso":42, 
            "Terras de Bouro":54,
            "Vieira do Minho":33, 
            "Vila Nova de Famalicão":52, 
            "Vila Verde":64,
            "Vizela":30
        }
        heuristicaEsposende= {
            "Amares":40,
            "Barcelos":13,
            "Braga":31,
            "Cabeceiras de Basto":60,
            "Celorico de Basto":65,
            "Esposende":1,
            "Fafe":62,
            "Guimarães":45,
            "Póvoa de Lanhoso":40, 
            "Terras de Bouro":53,
            "Vieira do Minho":57, 
            "Vila Nova de Famalicão":29, 
            "Vila Verde":27,
            "Vizela":49
        }
        heuristicasFafe= {
            "Amares":26,
            "Barcelos":50,
            "Braga":29,
            "Cabeceiras de Basto":26,
            "Celorico de Basto":19,
            "Esposende":62,
            "Fafe":1,
            "Guimarães":14,
            "Póvoa de Lanhoso":25, 
            "Terras de Bouro":41,
            "Vieira do Minho":28, 
            "Vila Nova de Famalicão":34, 
            "Vila Verde":33,
            "Vizela":18
        }
        heuristicasGuimaraes= {
            "Amares":28,
            "Barcelos":32,
            "Braga":20,
            "Cabeceiras de Basto":33,
            "Celorico de Basto":28,
            "Esposende":45,
            "Fafe":14,
            "Guimarães":1,
            "Póvoa de Lanhoso":23, 
            "Terras de Bouro":47,
            "Vieira do Minho":31, 
            "Vila Nova de Famalicão":23, 
            "Vila Verde":38,
            "Vizela":13
        }
        heuristicasLanhoso= {
            "Amares":11,
            "Barcelos":33,
            "Braga":14,
            "Cabeceiras de Basto":25,
            "Celorico de Basto":42,
            "Esposende":40,
            "Fafe":25,
            "Guimarães":23,
            "Póvoa de Lanhoso":1, 
            "Terras de Bouro":17,
            "Vieira do Minho":14, 
            "Vila Nova de Famalicão":33, 
            "Vila Verde":20,
            "Vizela":30
        }
        heuristicasBouro= {
            "Amares":13,
            "Barcelos":44,
            "Braga":34,
            "Cabeceiras de Basto":40,
            "Celorico de Basto":54,
            "Esposende":53,
            "Fafe":41,
            "Guimarães":47,
            "Póvoa de Lanhoso":17, 
            "Terras de Bouro":1,
            "Vieira do Minho":20, 
            "Vila Nova de Famalicão":64, 
            "Vila Verde":19,
            "Vizela":59
        }
        heuristicasVieiraDoMinho= {
            "Amares":21,
            "Barcelos":51,
            "Braga":28,
            "Cabeceiras de Basto":18,
            "Celorico de Basto":33,
            "Esposende":57,
            "Fafe":28,
            "Guimarães":31,
            "Póvoa de Lanhoso":14, 
            "Terras de Bouro":20,
            "Vieira do Minho":1, 
            "Vila Nova de Famalicão":56, 
            "Vila Verde":31,
            "Vizela":41
        }
        heuristicasFamalicao= {
            "Amares":32,
            "Barcelos":26,
            "Braga":23,
            "Cabeceiras de Basto":57,
            "Celorico de Basto":52,
            "Esposende":29,
            "Fafe":34,
            "Guimarães":23,
            "Póvoa de Lanhoso":33, 
            "Terras de Bouro":64,
            "Vieira do Minho":56, 
            "Vila Nova de Famalicão":1, 
            "Vila Verde":34,
            "Vizela":21
        }
        heuristicasVilaVerde= {
            "Amares":9,
            "Barcelos":25,
            "Braga":13,
            "Cabeceiras de Basto":40,
            "Celorico de Basto":64,
            "Esposende":27,
            "Fafe":33,
            "Guimarães":38,
            "Póvoa de Lanhoso":20, 
            "Terras de Bouro":19,
            "Vieira do Minho":31, 
            "Vila Nova de Famalicão":34, 
            "Vila Verde":1,
            "Vizela":47
        }
        heuristicasVizela= {
            "Amares":32,
            "Barcelos":37,
            "Braga":28,
            "Cabeceiras de Basto":38,
            "Celorico de Basto":30,
            "Esposende":49,
            "Fafe":18,
            "Guimarães":11,
            "Póvoa de Lanhoso":30, 
            "Terras de Bouro":59,
            "Vieira do Minho":41, 
            "Vila Nova de Famalicão":21, 
            "Vila Verde":47,
            "Vizela":1
        }
        self.heuristicas.append(heuristicasBraga)
        self.heuristicas.append(heuristicasAmares)
        self.heuristicas.append(heuristicasBarcelos)
        self.heuristicas.append(heuristicasCabeceiras)
        self.heuristicas.append(heuristicasCelorico)
        self.heuristicas.append(heuristicaEsposende)
        self.heuristicas.append(heuristicasFafe)
        self.heuristicas.append(heuristicasGuimaraes)
        self.heuristicas.append(heuristicasLanhoso)
        self.heuristicas.append(heuristicasBouro)
        self.heuristicas.append(heuristicasVieiraDoMinho)
        self.heuristicas.append(heuristicasFamalicao)
        self.heuristicas.append(heuristicasVilaVerde)
        self.heuristicas.append(heuristicasVizela)

    def getHeu(self, name, dest):
        for heu in self.heuristicas:
            if heu[name] == 1:
                return heu[dest]
        return 0

