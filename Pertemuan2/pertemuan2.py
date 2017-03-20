graph = {'Hariang': ['Tanjung Kerta', 'Buahdua','Sanca'],
             'Tanjung Kerta': ['Hariang', 'Cimalaka'],
             'Cimalaka': ['Tanjung Kerta','Cibeureum'],
             'Cibeureum': ['Cimalaka','Legok'],
             'Legok': ['Cibeureum','Conggeang'],
             'Conggeang': ['Legok','Buahdua'],
             'Buahdua': ['Hariang', 'Sanca', 'Conggeang'],
             'Sanca': ['Buahdua', 'Hariang'],
         }
 
def jalur_terpendek(graph, awal, tujuan, jalur=[]):
        jalur = jalur + [awal]
        if awal == tujuan:
            return jalur
        if not graph.has_key(awal):
            return None
        jalurpendek = None
        for node in graph[awal]:
            if node not in jalur:
                newjalur = jalur_terpendek(graph, node, tujuan, jalur)
                if newjalur:
                    if not jalurpendek or len(newjalur) < len(jalurpendek):
                        jalurpendek = newjalur
        return jalurpendek
print("Jalur Kecamatan di Kabupaten Sumedang")
print ("(Hariang,Tanjung Kerta,Cimalaka,Cibeureum)")
print ("(Legok,Conggeang,Buahdua,Sanca)")
print ("\n")
awal = raw_input("Titik Awal : ")
tujuan = raw_input("Titik Tujuan : ")
hasil = jalur_terpendek(graph, awal, tujuan, jalur=[])
print "Jalur Terpendek", hasil