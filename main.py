from rich.console import Console
from rich.markdown import Markdown
from chain.rantai import respon


console = Console()
print("Halo nama saya Anji Ai yang akan menjawab semua pertanyaanmu 😄")
masuk_user = input("Ingin bahas topik apa hari ini? ")
hasil = respon(masuk_user)
out_for = f"""
      Topik tentang {masuk_user.capitalize()}
      
      Definisi:
      {hasil.definisi}
      
      Contoh:
      {hasil.contoh}
      """
console.print(Markdown(out_for))