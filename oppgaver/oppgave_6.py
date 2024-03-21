from oppgaver.utils import query, insert, insert_return_rowID

def best_seller():
    # SQL query
    query_str = """
        SELECT TeaterStykke.navnPaStykke AS Forestillingsnavn, 
               f.dato AS Spilldato, 
               COUNT(b.BillettID) AS AntallSolgteBilletter
        FROM Forestilling AS f
        INNER JOIN Teaterstykke ON f.navnPaStykke = Teaterstykke.navnPaStykke
        LEFT JOIN Billett AS b ON b.ForestillingID = f.ForestillingID
        GROUP BY f.dato, Teaterstykke.navnPaStykke
        ORDER BY AntallSolgteBilletter DESC
    """
    
    # Execute query using utils function
    stykker = query(query_str)
    
    return stykker

def print_best_sellers(plays):
    print("    Bestselgende forestillinger:")
    print(" " * 4 + "{:<30} {:<20} {:<10}".format("Forestilling", "Dato", "Antall solgte plasser"))
    print(" " * 4 + "-" * 60)
    for play in plays:
        forestillingsnavn = play[0]
        spilldato = play[1]
        antall_solgte_billetter = play[2]
        print(" " * 4 + "{:<30} {:<20} {:<10}".format(forestillingsnavn, spilldato, antall_solgte_billetter))

def print_bestselgere():
    plays = best_seller()
    print_best_sellers(plays)

if __name__ == "__main__":
    print_bestselgere()