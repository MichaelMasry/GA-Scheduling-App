from Operation import Operation


class Job:
    def __init__(self, start_date, goal_date, model, batchsize, job_id):
        self.start_date = start_date
        self.goal_date = goal_date
        self.model = model
        self.operations = []
        self.batchsize = batchsize
        self.job_id = job_id

        if model == "ALKAPRESS 10MG 30 TAB":
            o1 = Operation("Blending3 50 kg", "Drum Mixer", 2.5, job_id)
            o2 = Operation("Blending1 400 kg", "Shangy-UH", 2, job_id)
            o3 = Operation("Sifter", "Sifter", 2, job_id)
            o4 = Operation("Blending1 400 kg", "Shangy-UH", 2, job_id)
            o5 = Operation("Compression1", "Kilian", 14.32, job_id)  # CHECK
            self.operations.extend([o1, o2, o3, o4, o5])
            o2.dependencies = [o1]
            o3.dependencies = [o2]
            o4.dependencies = [o3]
            o5.dependencies = [o4]

        elif model == "ALKAPRESS 5MG 20TAB":
            o1 = Operation("Blending3 50 kg", "Drum Mixer", 2.5, job_id)
            o2 = Operation("Blending1 400 kg", "Shangy-UH", 2, job_id)
            o3 = Operation("Sifter", "Sifter", 2, job_id)
            o4 = Operation("Blending1 400 kg", "Shangy-UH", 2, job_id)
            o5 = Operation("Compression2", "FetaIC", 14.32, job_id)

            self.operations.extend([o1, o2, o3, o4, o5])
            o2.dependencies = [o1]
            o3.dependencies = [o2]
            o4.dependencies = [o3]
            o5.dependencies = [o4]

        elif model == "ALKAPRESS 5MG 30 TAB":
            o1 = Operation("Blending3 50 kg", "Drum Mixer", 2.5, job_id)
            o2 = Operation("Blending1 400 kg", "Shangy-UH", 2, job_id)
            o3 = Operation("Sifter", "Sifter", 2, job_id)
            o4 = Operation("Blending1 400 kg", "Shangy-UH", 2, job_id)
            o5 = Operation("Compression2", "FetaIC", 14.32, job_id)

            self.operations.extend([o1, o2, o3, o4, o5])
            o2.dependencies = [o1]
            o3.dependencies = [o2]
            o4.dependencies = [o3]
            o5.dependencies = [o4]

        elif model == "ALKAPRESS PLUS 10/160":
            o1 = Operation("Blending3 50 kg", "Drum Mixer", 5, job_id)
            o2 = Operation("Blending1 400 kg", "Shangy-UH", 2, job_id)
            o3 = Operation("Compactor", " Compactor", 13, job_id)
            o4 = Operation("Blending2 200kg", "Double Cone", 2, job_id)
            o5 = Operation("Compression1", "Kilian", 14.32, job_id)
            o6 = Operation("Coating1 400 kg", "SeJungCoating", 6, job_id)

            self.operations.extend([o1, o2, o3, o4, o5, o6])
            o2.dependencies = [o1]
            o3.dependencies = [o2]
            o4.dependencies = [o3]
            o5.dependencies = [o4]
            o6.dependencies = [o5]

        elif model == "ALKAPRESS PLUS 5/160MG":
            o1 = Operation("Blending3 50 kg", "Drum Mixer", 5, job_id)
            o2 = Operation("Blending1 400 kg", "Shangy-UH", 2, job_id)
            o3 = Operation("Compactor", " Compactor", 13, job_id)
            o4 = Operation("Blending1 400 kg", "Shangy-UH", 2, job_id)
            o5 = Operation("Compression1", "Kilian", 14.32, job_id)
            o6 = Operation("Coating1 400 kg", "SeJungCoating", 6, job_id)

            self.operations.extend([o1, o2, o3, o4, o5, o6])
            o2.dependencies = [o1]
            o3.dependencies = [o2]
            o4.dependencies = [o3]
            o5.dependencies = [o4]
            o6.dependencies = [o5]

        elif model == "ALKOR 10/20MG Suecal 14 tab":
            o1 = Operation("Kneading1 max limit", "ComasaKneading", 1.5, job_id)
            o2 = Operation("Kneading2 min limit", "SeJungKneading", 1, job_id)
            o3 = Operation("Drying", "Oven", 7, job_id)
            o4 = Operation("Fitz Sifter", "Fitz Sifter", 4, job_id)
            o5 = Operation("Blending2 200kg", "Double Cone", 1.5, job_id)
            o6 = Operation("Compression3", "FetaI", 4, job_id)
            self.operations.extend([o1, o2, o3, o4, o5, o6])
            o2.dependencies = [o1]
            o3.dependencies = [o2]
            o4.dependencies = [o3]
            o5.dependencies = [o4]
            o6.dependencies = [o5]

        elif model == "ALKOR 10/40MG Suecal 14 tab":
            o1 = Operation("Kneading1 max limit", "ComasaKneading", 1.5, job_id)
            o2 = Operation("Kneading2 min limit", "SeJungKneading", 1, job_id)
            o3 = Operation("Drying", "Oven", 7, job_id)
            o4 = Operation("Fitz Sifter", "Fitz Sifter", 4, job_id)
            o5 = Operation("Blending2 200kg", "Double Cone", 1.5, job_id)
            o6 = Operation("Compression3", "FetaI", 4, job_id)
            self.operations.extend([o1, o2, o3, o4, o5, o6])
            o2.dependencies = [o1]
            o3.dependencies = [o2]
            o4.dependencies = [o3]
            o5.dependencies = [o4]
            o6.dependencies = [o5]

        elif model == "BISTOL 10MG 20TAB":
            o1 = Operation("Kneading1 max limit", "ComasaKneading", 1, job_id)
            o2 = Operation("Blending3 50 kg", "Drum Mixer", 2, job_id)
            o3 = Operation("Compression3", "FetaI", 4, job_id)
            o4 = Operation("Coating2 120 kg", "Airpack", 4.5, job_id)
            self.operations.extend([o1, o2, o3, o4])
            o2.dependencies = [o1]
            o3.dependencies = [o2]
            o4.dependencies = [o3]

        elif model == "BISTOL 10MG 20TAB TENDER ":
            o1 = Operation("Kneading1 max limit", "ComasaKneading", 1, job_id)
            o2 = Operation("Blending3 50 kg", "Drum Mixer", 2, job_id)
            o3 = Operation("Compression3", "FetaI", 4, job_id)
            o4 = Operation("Coating2 120 kg", "Airpack", 4.5, job_id)
            self.operations.extend([o1, o2, o3, o4])
            o2.dependencies = [o1]
            o3.dependencies = [o2]
            o4.dependencies = [o3]

        elif model == "BISTOL 2.5MG 20TAB":
            o1 = Operation("Kneading1 max limit", "ComasaKneading", 1, job_id)
            o2 = Operation("Blending3 50 kg", "Drum Mixer", 2, job_id)
            o3 = Operation("Compression3", "FetaI", 4, job_id)
            o4 = Operation("Coating2 120 kg", "Airpack", 4.5, job_id)
            self.operations.extend([o1, o2, o3, o4])
            o2.dependencies = [o1]
            o3.dependencies = [o2]
            o4.dependencies = [o3]

        elif model == "CIPROBAY 250":
            o1 = Operation("Blending3 50 kg", "Drum Mixer", 1, job_id)
            o2 = Operation("Compression3", "FetaI", 4, job_id)
            o3 = Operation("Coating2 120 kg", "Airpack", 5, job_id)
            self.operations.extend([o1, o2, o3])
            o2.dependencies = [o1]
            o3.dependencies = [o2]

        elif model == "CIPROBAY 500MG":
            o1 = Operation("Blending1 400 kg", "Shangy-UH", 2, job_id)
            o2 = Operation("Compression3", "FetaI", 4, job_id)
            o3 = Operation("Coating1 400 kg", "SeJungCoating", 7, job_id)
            self.operations.extend([o1, o2, o3])
            o2.dependencies = [o1]
            o3.dependencies = [o2]

        elif model == "CIPROBAY 750MG":
            o1 = Operation("Blending1 400 kg", "Shangy-UH", 2, job_id)
            o2 = Operation("Compression3", "FetaI", 4, job_id)
            o3 = Operation("Coating2 120 kg", "Airpack", 9, job_id)
            self.operations.extend([o1, o2, o3])
            o2.dependencies = [o1]
            o3.dependencies = [o2]

        elif model == "XANOXIBAN 15 MG 50TAB":
            o1 = Operation("Blending3 50 kg", "Drum Mixer", 1, job_id)
            o2 = Operation("Coating1 400 kg", "SeJungCoating", 2, job_id)
            o3 = Operation("Drying", "Oven", 7, job_id)
            o4 = Operation(" Milling", "Milling", 2, job_id)
            o5 = Operation("Blending3 50 kg", "Drum Mixer", 1, job_id)
            o6 = Operation("Compression3", "FetaI", 4, job_id)
            o7 = Operation("Coating3 50 kg", "Fayrouz", 7, job_id)  # GANSON COATER
            self.operations.extend([o1, o2, o3, o4, o5, o6, o7])
            o2.dependencies = [o1]
            o3.dependencies = [o2]
            o4.dependencies = [o3]
            o5.dependencies = [o4]
            o6.dependencies = [o5]
            o7.dependencies = [o6]

        elif model == "XANOXIBAN 20 MG 30TAB":
            o1 = Operation("Blending3 50 kg", "Drum Mixer", 1, job_id)
            o2 = Operation("Coating1 400 kg", "SeJungCoating", 2, job_id)
            o3 = Operation("Drying", "Oven", 7, job_id)
            o4 = Operation(" Milling", "Milling", 2, job_id)
            o5 = Operation("Blending3 50 kg", "Drum Mixer", 1, job_id)
            o6 = Operation("Compression3", "FetaI", 4, job_id)
            o7 = Operation("Coating3 50 kg", "Fayrouz", 7, job_id)  # GANSON COATER
            self.operations.extend([o1, o2, o3, o4, o5, o6, o7])
            o2.dependencies = [o1]
            o3.dependencies = [o2]
            o4.dependencies = [o3]
            o5.dependencies = [o4]
            o6.dependencies = [o5]
            o7.dependencies = [o6]

        elif model == "SUVIKAN 10MG 14 TAB ":
            o1 = Operation("Kneading1 max limit", "ComasaKneading", 1, job_id)
            o2 = Operation("Blending3 50 kg", "Drum Mixer", 2, job_id)
            o3 = Operation("Compression3", "FetaI", 4, job_id)
            o4 = Operation("Coating2 120 kg", "Airpack", 5, job_id)
            self.operations.extend([o1, o2, o3, o4])
            o2.dependencies = [o1]
            o3.dependencies = [o2]
            o4.dependencies = [o3]

        elif model == "SUVIKAN 20MG 14 TAB ":
            o1 = Operation("Kneading1 max limit", "ComasaKneading", 1, job_id)
            o2 = Operation("Blending3 50 kg", "Drum Mixer", 2, job_id)
            o3 = Operation("Compression3", "FetaI", 4, job_id)
            o4 = Operation("Coating2 120 kg", "Airpack", 5, job_id)
            self.operations.extend([o1, o2, o3, o4])
            o2.dependencies = [o1]
            o3.dependencies = [o2]
            o4.dependencies = [o3]

        elif model == "LYROLIN 50MG 30 CAP":
            o1 = Operation("Blending3 50 kg", "Drum Mixer", 1.5, job_id)
            o2 = Operation("Fitz", "Fitz", 1.5, job_id)
            o3 = Operation("Encapsulation3", "Bosch", 1, job_id)
            o4 = Operation("Encapsulation1", "PAM25", 8, job_id)
            self.operations.extend([o1, o2, o3, o4])
            o2.dependencies = [o1]
            o3.dependencies = [o2]
            o4.dependencies = [o3]

        elif model == "LYROLIN 75MG 20 CAP":
            # No info about this product
            pass

        elif model == "LYROLIN 75MG 30 CAP":
            o1 = Operation("Blending2 200kg", "Double Cone", 2, job_id)
            o2 = Operation("Fitz", "Fitz", 4, job_id)
            o3 = Operation("Encapsulation3", "Bosch", 1, job_id)
            o4 = Operation("Encapsulation1", "PAM25", 8, job_id)
            self.operations.extend([o1, o2, o3, o4])
            o2.dependencies = [o1]
            o3.dependencies = [o2]
            o4.dependencies = [o3]

        elif model == "PEPZOL 40MG 14 CAP":
            o1 = Operation("Encapsulation2", "PAM90", 9, job_id)
            o2 = Operation("Encapsulation1", "PAM25", 8, job_id)
            self.operations.extend([o1, o2])
            o2.dependencies = [o1]

        elif model == "PEPZOL 40MG 14 CAP Tender":
            o1 = Operation("Encapsulation2", "PAM90", 9, job_id)
            o2 = Operation("Encapsulation1", "PAM25", 8, job_id)
            self.operations.extend([o1, o2])
            o2.dependencies = [o1]

        elif model == "PEPZOL 40MG 7 CAP":
            o1 = Operation("Encapsulation2", "PAM90", 9, job_id)
            o2 = Operation("Encapsulation1", "PAM25", 8, job_id)
            self.operations.extend([o1, o2])
            o2.dependencies = [o1]

    def print_operations(self):
        for op in self.operations:
            print(str(op) + "\n")

    def print_product(self):
        print(" Medicine name: " + str(self.model)
              + "\t Batch Size: " + str(self.batchsize))
