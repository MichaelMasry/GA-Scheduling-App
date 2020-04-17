import pandas as pd


class Product:

    def __init__(self, name, excel):
        self.name = str(name)
        self.product_data = []
        data = pd.read_excel(excel)
        df = pd.DataFrame(data)
        product_info = df.loc[df['Description'] == self.name]
        self.FN_batch_size = float(product_info["FN St. Batch size"])
        self.bulk_size_per_kg = float(product_info["Bulk size/kg"])
        self.pack_size_per_blister = float(product_info["Pack size/ blister"])
        self.number_of_tablet_per_pack = float(product_info["No. of Tablet/ pack"])
        self.blistering_rate = float(product_info["Blistering/cartooning  Rate "])
        self.number_of_batches = (self.FN_batch_size // self.bulk_size_per_kg)
        self.FTE = float(product_info["FTE'S "])

    def info(self):
        out = "Number of batches: ", self.number_of_batches, "\n", "FN_batch_size: ", self.FN_batch_size, "\n" \
            , "Bulk size per kg: ", \
              self.bulk_size_per_kg, "\n", "Pack size per blister: ", self.pack_size_per_blister, "\n", \
              "Number of tablet per pack: ", self.number_of_tablet_per_pack \
            , "\n", "Blistering rate: ", self.blistering_rate, "\n", "FTE: ", self.FTE
        return out
