__author__ = "crypto"

# Database Terminology
"""
    Database:
        The container for all data that you store.
   
    In SQLite, the entire database is stored in a single file.
   
    Database Dictionary: provides a comprehensive list of the structure and
                        types of data in the database.     
    
    Table:
        a collection of related data held in the database.
    
    Field: 
        the basic unit of data in a table.
        Example:
            Sku; Name; Description; Image; price    <--- first row in any database.
        
        Another field types can often called "Blobs" which support to stand for binary
        large objects.
    
    Column: 
        is another name for "field" refer to a single vertical record
        
    Row:
        a single set of data containing all the columns in the table
        
    Flat File database:
        stores all the data in a single table, the result could be a lots of duplicates.
        
    Normalization:
        Is basically the process of removing the redundant duplicated and irrelevant data
        from the tables.
        
                                                    Invoices
                    Invoice; Date; Description; Amount; Name; Address; Credit_limit; Balance
                    
                            Customer                                                Invoices
    Norm01:     Name; Address; Credit_limit; Balance        ||      Invoice; Date; Description; Amount; Name


                            Customer                              Customer_Invoices                               Invoices
    Norm02:     Name; Address; Credit_limit; Balance       ||   Customer_name; Invoice     ||      Invoice; Date; Description; Amount; Name

    
    View: 
        is a selection of rows and columns, possible from more that one table. 
"""