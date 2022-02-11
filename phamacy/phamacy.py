from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter

class PhamacyManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")



# ================================ addMed variable =======================================
        self.addmed_var=StringVar()
        self.refmed_var=StringVar()

# =============================== Main Variable ==================================
        self.ref_var=StringVar()
        self.cmpName_var=StringVar()
        self.typeMed_var=StringVar()
        self.medName_var=StringVar()
        self.lot_var=StringVar()
        self.issuedate_var=StringVar()
        self.expdate_var=StringVar()
        self.uses_var=StringVar()
        self.sideEffect_var=StringVar()
        self.warning_var=StringVar()
        self.dosage_var=StringVar()
        self.price_var=StringVar()
        self.product_var=StringVar()

        lbltitle=Label(self.root,text="PHARMACY MANAGEMENT SYSTEM",bd=15,relief=RIDGE,bg="white",fg="darkgreen",font=("times new roman",50,"bold"),padx=2,pady=4)
        lbltitle.pack(side=TOP,fill=X)

        img1=Image.open(r"C:\Users\Isuru Dilshan\Desktop\python\phamacyMS\Image\pharmacy.png")
        img1=img1.resize((100,80),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0,bg="white")
        b1.place(x=60,y=16)

        # ======================== DataFrame ====================================
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=120,width=1530,height=400)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Information",fg="darkgreen",font=("arial",14,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        DataFrameRight = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=20, text="Medicine Add Department", fg="darkgreen",font=("arial", 15, "bold"))
        DataFrameRight.place(x=910, y=5, width=540, height=350)

        # ======================== ButtonsFrame =================================
        ButtonFrame = Frame(self.root, bd=15, relief=RIDGE, padx=20)
        ButtonFrame.place(x=0, y=520, width=1530, height=65)

        # ======================== MainFrame ===================================
        btnAddData=Button(ButtonFrame,command=self.Add_data,text="ADD MEDICINE",font=("arial", 13, "bold"),bg="darkgreen",fg="white")
        btnAddData.grid(row=0,column=0)

        btnUpdateMed = Button(ButtonFrame,command=self.Update,text="UPDATE", font=("arial", 13, "bold"),width=14,bg="darkgreen", fg="white")
        btnUpdateMed.grid(row=0, column=1)

        btnDeleteMed = Button(ButtonFrame,command=self.delete,text="DELETE", font=("arial", 13, "bold"),width=14,bg="red", fg="white")
        btnDeleteMed.grid(row=0, column=2)

        btnResetMed = Button(ButtonFrame,command=self.reset,text="RESET", font=("arial", 13, "bold"),width=14,bg="darkgreen", fg="white")
        btnResetMed.grid(row=0, column=3)

        btnExitMed = Button(ButtonFrame,command=self.Exit,text="EXIT", font=("arial", 13, "bold"),width=14,bg="darkgreen", fg="white")
        btnExitMed.grid(row=0, column=4)

        # ======================== Search By =========================================
        lblSearch=Label(ButtonFrame,font=("arial",17,"bold"),text="Search By",padx=2,bg="red",fg="white")
        lblSearch.grid(row=0,column=5,sticky=W)

        self.search_var = StringVar()
        search_combo=ttk.Combobox(ButtonFrame,textvariable=self.search_var,width=13,font=("times new roman",17,"bold"),state="readonly")
        search_combo["values"]=("Ref","Medname","Lot")
        search_combo.grid(row=0,column=6)
        search_combo.current(0)

        self.searchTxt_var = StringVar()
        txtSearch=Entry(ButtonFrame,textvariable=self.searchTxt_var,bd=3,relief=RIDGE,width=12,font=("times new roman",17,"bold"))
        txtSearch.grid(row=0,column=7)

        searchBtn= Button(ButtonFrame,command=self.search_data,text="SEARCH", font=("arial", 13, "bold"), width=13, bg="darkgreen",fg="white")
        searchBtn.grid(row=0, column=8)

        showAll = Button(ButtonFrame,command=self.fatch_data,text="SHOW ALL", font=("arial", 13, "bold"), width=13, bg="darkgreen", fg="white")
        showAll.grid(row=0, column=9)

        # ========================lable and entry ==========================================
        lblrefno = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Reference No", padx=2)
        lblrefno.grid(row=0, column=0, sticky=W)

        conn = mysql.connector.connect(host="localhost", username="root", password="7986@1223Id", database="pharmacy")
        my_cursor = conn.cursor()
        my_cursor.execute("select Ref from pharma")
        row=my_cursor.fetchall()

        ref_combo = ttk.Combobox(DataFrameLeft,textvariable=self.ref_var,width=27,font=("arial", 12, "bold"), state="readonly")
        ref_combo["values"] = row
        ref_combo.grid(row=0, column=1)
        ref_combo.current(0)

        lblCompName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Company Name", padx=2)
        lblCompName.grid(row=1, column=0, sticky=W)
        txtCompName= Entry(DataFrameLeft,textvariable=self.cmpName_var,font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtCompName.grid(row=1, column=1)

        lblTypeMed = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Type Of Medicine", padx=2)
        lblTypeMed.grid(row=2, column=0, sticky=W)

        TypeMed_combo = ttk.Combobox(DataFrameLeft,textvariable=self.typeMed_var,width=27, font=("arial", 12, "bold"), state="readonly")
        TypeMed_combo["values"] = ("Tablet", "Liquid", "Capsules","Topical Medicines","Drops","Inhales","Injection")
        TypeMed_combo.current(0)
        TypeMed_combo.grid(row=2, column=1)

        # ========================= AddMedicine =============================================
        lblMedicineName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Medicine Name:", padx=2,pady=6)
        lblMedicineName.grid(row=3, column=0, sticky=W)

        conn = mysql.connector.connect(host="localhost", username="root", password="7986@1223Id", database="pharmacy")
        my_cursor = conn.cursor()
        my_cursor.execute("select MedName from pharma")
        med=my_cursor.fetchall()

        comMedicineName = ttk.Combobox(DataFrameLeft,textvariable=self.medName_var,width=27, font=("arial", 12, "bold"), state="readonly")
        comMedicineName["values"] = med
        comMedicineName.current(0)
        comMedicineName.grid(row=3, column=1)

        lblLotNo = Label(DataFrameLeft,font=("arial", 12, "bold"), text="Lot No:", padx=2, pady=6)
        lblLotNo.grid(row=4, column=0, sticky=W)
        txtLotNo =Entry(DataFrameLeft,textvariable=self.lot_var,font=("arial", 13, "bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtLotNo.grid(row=4,column=1)

        lblIssueDate = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblIssueDate.grid(row=5, column=0, sticky=W)
        txtIssueDate = Entry(DataFrameLeft,textvariable=self.issuedate_var,font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtIssueDate.grid(row=5, column=1)

        lblExDate = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Exp Date:", padx=2, pady=6)
        lblExDate.grid(row=6, column=0, sticky=W)
        txtExpDate = Entry(DataFrameLeft,textvariable=self.expdate_var,font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtExpDate.grid(row=6, column=1)

        lblUsers = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Uses:", padx=2, pady=6)
        lblUsers.grid(row=7, column=0, sticky=W)
        txtUsers = Entry(DataFrameLeft,textvariable=self.uses_var,font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtUsers.grid(row=7, column=1)

        lblSideEffect = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Side Effect:", padx=2, pady=6)
        lblSideEffect.grid(row=8, column=0, sticky=W)
        txtSideEffect = Entry(DataFrameLeft,textvariable=self.sideEffect_var,font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtSideEffect.grid(row=8, column=1)

        lblPrecWarning = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Prec&Warning:", padx=15)
        lblPrecWarning.grid(row=0, column=2, sticky=W)
        txtPrecWarning = Entry(DataFrameLeft,textvariable=self.warning_var,font=("arial", 12, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtPrecWarning.grid(row=0, column=3)

        lblDosage = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Dosage:", padx=15, pady=6)
        lblDosage.grid(row=1, column=2, sticky=W)
        txtDosage = Entry(DataFrameLeft,textvariable=self.dosage_var,font=("arial", 12, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtDosage.grid(row=1, column=3)

        lblPrice = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Tablet Price:", padx=15, pady=6)
        lblPrice.grid(row=2, column=2, sticky=W)
        txtPrice = Entry(DataFrameLeft,textvariable=self.price_var,font=("arial", 12, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtPrice.grid(row=2, column=3)

        lblProductQT = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Product QT:", padx=15, pady=6)
        lblProductQT.grid(row=3, column=2, sticky=W)
        txtProductQT = Entry(DataFrameLeft,textvariable=self.product_var,font=("arial", 12, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtProductQT.grid(row=3, column=3,sticky=W)

        # ================================= Image ==============================================
        lblhome = Label(DataFrameLeft, font=("arial", 16, "bold"), text="Stay Home Stay Safe", padx=2, pady=6,bg="white",fg="red",width=33)
        lblhome.place(x=420,y=130)

        img2 = Image.open(r"C:\Users\Isuru Dilshan\Desktop\python\phamacyMS\Image\med.jpg")
        img2 = img2.resize((150,135), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        b1 = Button(self.root, image=self.photoimg2, borderwidth=0, bg="white")
        b1.place(x=475, y=330)

        img3 = Image.open(r"C:\Users\Isuru Dilshan\Desktop\python\phamacyMS\Image\Pharmacy.jpg")
        img3 = img3.resize((150, 135), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        b1 = Button(self.root, image=self.photoimg3, borderwidth=0, bg="white")
        b1.place(x=620, y=330)

        img4 = Image.open(r"C:\Users\Isuru Dilshan\Desktop\python\phamacyMS\Image\image.jpg")
        img4 = img4.resize((150, 135), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1 = Button(self.root, image=self.photoimg4, borderwidth=0, bg="white")
        b1.place(x=771, y=330)

        # ============================= dataframeRight =========================================
        DataFrameRight = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=20, text=" New Medicine Add Department",fg="darkgreen", font=("arial", 14, "bold"))
        DataFrameRight.place(x=910, y=5, width=540, height=350)

        img5 = Image.open(r"C:\Users\Isuru Dilshan\Desktop\python\phamacyMS\Image\t.png")
        img5 = img5.resize((200, 75), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1 = Button(self.root, image=self.photoimg5, borderwidth=0, bg="white")
        b1.place(x=960, y=165)

        img6 = Image.open(r"C:\Users\Isuru Dilshan\Desktop\python\phamacyMS\Image\t.png")
        img6 = img6.resize((200, 75), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b1 = Button(self.root, image=self.photoimg6, borderwidth=0, bg="white")
        b1.place(x=1160, y=165)

        img7 = Image.open(r"C:\Users\Isuru Dilshan\Desktop\python\phamacyMS\Image\Pre.jpg")
        img7 = img7.resize((200, 147), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b1 = Button(self.root, image=self.photoimg7, borderwidth=0, bg="white")
        b1.place(x=1270, y=165)

        lblrefno = Label(DataFrameRight, font=("times new roman", 14), text="Reference No:", padx=0, pady=6)
        lblrefno.place(x=0,y=80)
        txtrefno = Entry(DataFrameRight,textvariable=self.refmed_var,font=("times new roman", 13), bg="white", bd=2, relief=RIDGE, width=17)
        txtrefno.place(x=135,y=80)

        lblmedName = Label(DataFrameRight, font=("times new roman", 14), text="Medicine Name:", padx=0, pady=6)
        lblmedName.place(x=0, y=110)
        txtmedName = Entry(DataFrameRight,textvariable=self.addmed_var,font=("times new roman", 13), bg="white", bd=2, relief=RIDGE, width=17)
        txtmedName.place(x=135, y=110)

        # =============================== side frame ================================
        side_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="white")
        side_frame.place(x=0,y=150,width=290,height=160)

        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y = ttk.Scrollbar(side_frame, orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)

        self.medicine_table=ttk.Treeview(side_frame,column=("ref","medname"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)

        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref",text="Ref")
        self.medicine_table.heading("medname", text="Medicine Name")

        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH,expand=1)

        self.medicine_table.column("ref",width=100)
        self.medicine_table.column("medname", width=100)

        self.medicine_table.bind("<ButtonRelease-1>",self.Medget_cursor)

        # =========================================== Medicine Add Button ================================
        down_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="darkgreen")
        down_frame.place(x=330,y=150,width=135,height=160)

        btnAddmed = Button(down_frame, text="INSERT",command=self.AddMed,font=("arial", 12, "bold"),width=12, bg="blue", fg="white",pady=4)
        btnAddmed.grid(row=0, column=0)

        btnUpdatemed = Button(down_frame, text="UPDATE",command=self.UpdateMed,font=("arial", 12, "bold"), width=12, bg="orange", fg="white",pady=4)
        btnUpdatemed.grid(row=1, column=0)

        btnDeletemed = Button(down_frame, text="DELETE",command=self.DeleteMed,font=("arial", 12, "bold"), width=12, bg="red", fg="white",pady=4)
        btnDeletemed.grid(row=2, column=0)

        btnClearmed = Button(down_frame, text="CLEAR",command=self.ClearMed,font=("arial", 12, "bold"), width=12, bg="purple", fg="white",pady=4)
        btnClearmed.grid(row=3, column=0)

        # ========================================= Frame Details ===========================================
        Framedetails=Frame(self.root,bd=15,relief=RIDGE)
        Framedetails.place(x=0,y=580,width=1530,height=210)

        # ========================================= Main Table & scrollbar =================================
        Table_frame = Frame(self.root, bd=15, relief=RIDGE,padx=20)
        Table_frame.place(x=15, y=595, width=1500, height=180)

        scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.pharmacy_table=ttk.Treeview(Table_frame,column=("reg","companyname","type","tabletname","lotno","issuedate","expdate","uses","sideeffect","warning",
                                                             "dosage","price","productqt")
                                                              ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)

        self.pharmacy_table["show"]="headings"

        self.pharmacy_table.heading("reg",text="Reference No")
        self.pharmacy_table.heading("companyname",text="Company Name")
        self.pharmacy_table.heading("type",text="Type Of Medicine")
        self.pharmacy_table.heading("tabletname",text="Table Name")
        self.pharmacy_table.heading("lotno",text="Lot No")
        self.pharmacy_table.heading("issuedate",text="Issue Date")
        self.pharmacy_table.heading("expdate",text="Exp Date")
        self.pharmacy_table.heading("uses",text="Uses")
        self.pharmacy_table.heading("sideeffect",text="Side Effect")
        self.pharmacy_table.heading("warning",text="Prec&Warning")
        self.pharmacy_table.heading("dosage",text="Dosage")
        self.pharmacy_table.heading("price",text="Price")
        self.pharmacy_table.heading("productqt",text="Product Qts")
        self.pharmacy_table.pack(fill=BOTH,expand=1)

        self.pharmacy_table.column("reg",width=100)
        self.pharmacy_table.column("companyname",width=100)
        self.pharmacy_table.column("type",width=100)
        self.pharmacy_table.column("tabletname",width=100)
        self.pharmacy_table.column("lotno",width=100)
        self.pharmacy_table.column("issuedate",width=100)
        self.pharmacy_table.column("expdate",width=100)
        self.pharmacy_table.column("uses",width=100)
        self.pharmacy_table.column("sideeffect",width=100)
        self.pharmacy_table.column("warning",width=100)
        self.pharmacy_table.column("dosage",width=100)
        self.pharmacy_table.column("price",width=100)
        self.pharmacy_table.column("productqt",width=100)
        self.fetch_dataMed()
        self.fatch_data()
        self.pharmacy_table.bind("<ButtonRelease-1>",self.get_cursor)

        # ======================== ADD Medicine Functionality Declaration ===============================

    def AddMed(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="7986@1223Id",database="pharmacy")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into pharma(Ref,MedName) values(%s,%s)",(
                                                                    self.refmed_var.get(),
                                                                    self.addmed_var.get(),
                                                                    ))
        conn.commit()
        self.fetch_dataMed()
        self.Medget_cursor()
        conn.close()
        messagebox.showinfo("Success","Medicine Added")

    def fetch_dataMed(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="7986@1223Id", database="pharmacy")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from pharma")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for i in rows:
                self.medicine_table.insert("",END,values=i)
            conn.commit()
        conn.close()

# =============================== MedGetcursor ==============================
    def Medget_cursor(self,event=""):
        cursor_row=self.medicine_table.focus()
        content=self.medicine_table.item(cursor_row)
        row=content["values"]
        self.refmed_var.set(row[0])
        self.addmed_var.set(row[1])

# ================================ MedUpdate ================================
    def UpdateMed(self):
        if self.refmed_var.get()==""or self.addmed_var.get()=="":
            messagebox.showerror("Error","All fields are Required")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="7986@1223Id",database="pharmacy")
            my_cursor = conn.cursor()
            my_cursor.execute("update pharma set MedName=%s where Ref=%s",(
                                                                          self.addmed_var.get(),
                                                                          self.refmed_var.get(),
                                                                     ))
            conn.commit()
            self.fetch_dataMed()
            conn.close()
            messagebox.showinfo("Success","Medicine has been Updated")

    def DeleteMed(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="7986@1223Id", database="pharmacy")
        my_cursor = conn.cursor()

        sql="delete from pharma where Ref=%s"
        val=(self.refmed_var.get(),)
        my_cursor.execute(sql,val)

        conn.commit()
        self.fetch_dataMed()
        conn.close()
        messagebox.showinfo("Success","Medicine has been Deleted")

    def ClearMed(self):
        self.refmed_var.set("")
        self.addmed_var.set("")

    # ============================= Main table =========================
    def Add_data(self):
        if self.ref_var.get()==""or self.lot_var.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="7986@1223Id", database="pharmacy")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into pharmacy values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                                                                                self.ref_var.get(),
                                                                                                self.cmpName_var.get(),
                                                                                                self.typeMed_var.get(),
                                                                                                self.medName_var.get(),
                                                                                                self.lot_var.get(),
                                                                                                self.issuedate_var.get(),
                                                                                                self.expdate_var.get(),
                                                                                                self.uses_var.get(),
                                                                                                self.sideEffect_var.get(),
                                                                                                self.warning_var.get(),
                                                                                                self.dosage_var.get(),
                                                                                                self.price_var.get(),
                                                                                                self.product_var.get()
                                                                                              ))
            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("Success","Data has been Inserted")

    def fatch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="7986@1223Id", database="pharmacy")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from pharmacy")
        row=my_cursor.fetchall()
        if len(row)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in row:
                self.pharmacy_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row = self.pharmacy_table.focus()
        content = self.pharmacy_table.item(cursor_row)
        row = content["values"]

        self.ref_var.set(row[0]),
        self.cmpName_var.set(row[1]),
        self.typeMed_var.set(row[2]),
        self.medName_var.set(row[3]),
        self.lot_var.set(row[4]),
        self.issuedate_var.set(row[5]),
        self.expdate_var.set(row[6]),
        self.uses_var.set(row[7]),
        self.sideEffect_var.set(row[8]),
        self.warning_var.set(row[9]),
        self.dosage_var.set(row[10]),
        self.price_var.set(row[11]),
        self.product_var.set(row[12])

    def Update(self):
            if self.ref_var.get() == "" or self.lot_var.get() == "":
                messagebox.showerror("Error", "All fields are Required")
            else:
                conn = mysql.connector.connect(host="localhost", username="root", password="7986@1223Id",database="pharmacy")
                my_cursor = conn.cursor()
                my_cursor.execute("update pharmacy set CmpName=%s,TypeMed=%s,Medname=%s,Lot=%s,Issuedate=%s,Expdate=%s,uses=%s,sideEffect=%s,warning=%s,dosage=%s,price=%s,product=%s where Ref_no=%s", (

                                                                                                                                                                                                self.cmpName_var.get(),
                                                                                                                                                                                                self.typeMed_var.get(),
                                                                                                                                                                                                self.medName_var.get(),
                                                                                                                                                                                                self.lot_var.get(),
                                                                                                                                                                                                self.issuedate_var.get(),
                                                                                                                                                                                                self.expdate_var.get(),
                                                                                                                                                                                                self.uses_var.get(),
                                                                                                                                                                                                self.sideEffect_var.get(),
                                                                                                                                                                                                self.warning_var.get(),
                                                                                                                                                                                                self.dosage_var.get(),
                                                                                                                                                                                                self.price_var.get(),
                                                                                                                                                                                                self.product_var.get(),
                                                                                                                                                                                                self.ref_var.get()
                                                                                                                                                                                                            ))
                conn.commit()
                self.fatch_data()
                conn.close()
                messagebox.showinfo("UPDATE", "Record has been Updated Successfully")

    def delete(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="7986@1223Id", database="pharmacy")
        my_cursor = conn.cursor()

        sql = "delete from pharmacy where Ref_no=%s"
        val = (self.ref_var.get(),)
        my_cursor.execute(sql, val)

        conn.commit()
        self.fatch_data()
        conn.close()
        messagebox.showinfo("Delete", "Record has been Deleted Successfully")

    def reset(self):
                    #self.ref_var.set(""),
                    self.cmpName_var.set(""),
                   # self.typeMed_var.set(""),
                    #self.medName_var.set(""),
                    self.lot_var.set(""),
                    self.issuedate_var.set(""),
                    self.expdate_var.set(""),
                    self.uses_var.set(""),
                    self.sideEffect_var.set(""),
                    self.warning_var.set(""),
                    self.dosage_var.set(r""),
                    self.price_var.set(r""),
                    self.product_var.set(r"")

    def Exit(self):
        Exit=tkinter.messagebox.askyesno("Pharmacy Management System","Do You Want To Exit")
        if Exit>0:
            self.root.destroy()
            return

    def search_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="7986@1223Id", database="pharmacy")
        my_cursor = conn.cursor()

        my_cursor.execute("select * from pharmacy where"+str(self.search_var.get())+" LIKE '%"+str(self.searchTxt_var.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in rows:
                self.pharmacy_table.insert("",END,values=i)
            conn.commit()
        conn.close()


if __name__== "__main__":
    root=Tk()
    obj=PhamacyManagementSystem(root)
    root.mainloop()