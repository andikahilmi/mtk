import streamlit as st
from fractions import Fraction
from sympy import Rational


def fitur_jumlah_n_sampai_m(a, r):
    st.subheader("Sekarang Anda bisa menghitung jumlah dari suku ke-n sampai suku ke-m.")
    
    # Input nilai n dan m
    n_awal = st.number_input("Masukkan suku awal (misal: 5)", min_value=1, step=1)
    n_akhir = st.number_input("Masukkan suku akhir (misal: 10)", min_value=1, step=1)

    if n_akhir < n_awal:
        st.error("❌ Suku akhir harus lebih besar atau sama dengan suku awal.")
    else:
        # Hitung jumlah suku dari n_awal hingga n_akhir
        if r == 1:
            total = a * (n_akhir - n_awal + 1)
        else:
            sn_akhir = a * ((r ** n_akhir - 1) / (r - 1))
            sn_awal_minus1 = a * ((r ** (n_awal - 1) - 1) / (r - 1))
            total = sn_akhir - sn_awal_minus1

        st.info(f"📌 Jumlah suku dari ke-{n_awal} sampai ke-{n_akhir} adalah: **{total}**")

def hitung_jumlah_n_m_geometri(a, r, n_awal, n_akhir):
    if r == 1:
        total = a * (n_akhir - n_awal + 1)
    else:
        sn_akhir = a * ((r ** n_akhir - 1) / (r - 1))
        sn_awal_minus1 = a * ((r ** (n_awal - 1) - 1) / (r - 1))
        total = sn_akhir - sn_awal_minus1
    
    return total


def tampilkan_Un_Sn(a, r, n):
    a_sym = Rational(a)
    r_sym = Rational(r)

    un = f"{a_sym} * ({r_sym})^{{{n - 1}}}"
    if r == 1:
        sn = f"{a_sym} * {n}"
    else:
        sn = f"{a_sym} * (({r_sym})^{{{n}}} - 1) / ({r_sym} - 1)"

    return un, sn

def hitung_a_r_dari_dua_suku(n1, u1, n2, u2):
    try:
        if n1 == n2:
            return None, None, "❌ Error: Kedua urutan suku tidak boleh sama."

        selisih_n = n2 - n1
        r = (u2 / u1) ** Fraction(1, selisih_n)
        a = u1 / (r ** (n1 - 1))

        return a, r, None
    except ZeroDivisionError:
        return None, None, "❌ Error: Pembagian dengan nol terdeteksi."
    except Exception as e:
        return None, None, f"❌ Error: {str(e)}"

# Fungsi untuk menghitung suku pertama (a) dan beda (b) dari dua suku
def hitung_a_b_dari_dua_suku(n1, u1, n2, u2):
    try:
        if n1 == n2:
            return None, None, "❌ Error: Kedua urutan suku tidak boleh sama."

        selisih_n = n2 - n1
        b = (u2 - u1) / selisih_n  # Beda (b)
        a = u1 - (n1 - 1) * b  # Suku pertama (a)

        return a, b, None
    except ZeroDivisionError:
        return None, None, "❌ Error: Pembagian dengan nol terdeteksi."
    except Exception as e:
        return None, None, f"❌ Error: {str(e)}"
    
# Fungsi untuk menghitung suku pertama (a) dan beda (b) dari dua Sn yang diketahui
def hitung_a_b_dari_dua_sn(sn1, n1, sn2, n2):
    try:
        selisih_n = n2 - n1
        b = (sn2 - sn1) / selisih_n  # Beda (b)
        a = sn1 - (n1 - 1) * b  # Suku pertama (a)

        return a, b, None
    except ZeroDivisionError:
        return None, None, "❌ Error: Pembagian dengan nol terdeteksi."
    except Exception as e:
        return None, None, f"❌ Error: {str(e)}"

def main():
    menu = ["Deret Aritmatika", "Deret Geometri", "Tentang Aplikasi", "Tim Penyusun"]
    choice = st.sidebar.radio("Pilih Menu", menu)

    if choice == "Deret Aritmatika":
        st.title("Kalkulator Deret Aritmatika \U0001F4D0")
    
        # Fitur 1: Menghitung a dan b dari dua suku
        st.subheader("🔢 Menghitung a dan b dari dua suku yang diketahui")
        with st.form("form_suku_aritmatika"):
            col1, col2 = st.columns(2)
            with col1:
                n1 = st.number_input("Urutan suku pertama (n₁)", min_value=1, value=1)
                u1_str = st.text_input("Nilai suku ke-n₁ (contoh: 3)", value="3")
            with col2:
                n2 = st.number_input("Urutan suku kedua (n₂)", min_value=1, value=2)
                u2_str = st.text_input("Nilai suku ke-n₂ (contoh: 7)", value="7")
            submitted_suku = st.form_submit_button("🔍 Hitung a dan b dari suku")

        if submitted_suku:
            try:
                u1 = Fraction(u1_str)
                u2 = Fraction(u2_str)
                a, b, error = hitung_a_b_dari_dua_suku(n1, u1, n2, u2)

                if error:
                    st.error(error)
                else:
                    st.success("✅ Perhitungan berhasil!")
                    st.markdown(f"**Suku pertama (a)** = `{round(float(a), 1)}`")
                    st.markdown(f"**Beda (b)** = `{round(float(b), 1)}`")

            except ValueError:
                st.error("❌ Masukkan pecahan atau angka yang valid!")

        # Fitur 2: Menghitung a dan b dari dua Sn yang diketahui
        st.subheader("🔢 Menghitung a dan b dari dua nilai Sn yang diketahui")
        with st.form("form_sn_aritmatika"):
            col1, col2 = st.columns(2)
            with col1:
                n1_sn = st.number_input("Urutan Sn pertama (n₁)", min_value=1, value=9)
                sn1 = st.number_input("Nilai Sₙ₁", value=117)
            with col2:
                n2_sn = st.number_input("Urutan Sn kedua (n₂)", min_value=1, value=31)
                sn2 = st.number_input("Nilai Sₙ₂", value=2108)
            submitted_sn = st.form_submit_button("🔍 Hitung a dan b dari Sn")

        if submitted_sn:
            a_val, b_val, error = hitung_a_b_dari_dua_sn(sn1, n1_sn, sn2, n2_sn)

            if error:
                st.error(error)
            else:
                st.success("✅ Perhitungan berhasil!")
                st.markdown(f"**Suku pertama (a)** = `{round(float(a_val), 1)}`")
                st.markdown(f"**Beda (b)** = `{round(float(b_val), 1)}`")

        st.markdown("---")

        st.subheader("🔢 Perhitungan suku ke-n dan jumlah suku")

        a_input = st.number_input("Masukkan suku pertama (a):", value=1.0)
        d_input = st.number_input("Masukkan beda (b atau d):", value=1.0)

        n = st.number_input("Tentukan suku ke-n:", min_value=1, step=1, key="n_suku")
        suku_ke_n = a_input + (n - 1) * d_input
        st.write(f"➡️ Nilai suku ke-{n} adalah: **{suku_ke_n:.1f}**")

        jumlah_n = n / 2 * (2 * a_input + (n - 1) * d_input)
        st.write(f"\U0001F4D8 Jumlah dari {n} suku pertama adalah: **{jumlah_n:.1f}**")

        st.markdown("---")

        st.subheader("🔢 Perhitungan suku ke-n sampai dengan suku ke m")

        n2 = st.number_input("Masukkan nilai suku ke-n untuk perhitungan jumlah n sampai m:", min_value=1, step=1, key="n_awal")
        m = st.number_input("Masukkan nilai suku ke-m (lebih dari atau sama dengan n):", min_value=n2, step=1)

        jmlh_nm = ((m - n2 + 1) / 2) * (2 * (a_input + (n2 - 1) * d_input) + (m - n2) * d_input)
        st.write(f"\U0001F9EE Jumlah dari suku ke-{n2} hingga ke-{m} adalah: **{jmlh_nm:.1f}**")

    elif choice == "Deret Geometri":
       if choice == "Deret Geometri":
        st.title("\U0001F4D0 Kalkulator Deret Geometri")
        st.markdown("Masukkan dua suku acak dari deret geometri untuk menghitung suku pertama `(a)` dan rasio `(r)`.")

        # Input untuk dua suku dari deret geometri
        col1, col2 = st.columns(2)
        with col1:
            n1 = st.number_input("Urutan suku pertama (n₁)", min_value=1, value=3)
            u1_str = st.text_input("Nilai suku ke-n₁ (contoh: 3/4)", value="3/4")
        with col2:
            n2 = st.number_input("Urutan suku kedua (n₂)", min_value=1, value=5)
            u2_str = st.text_input("Nilai suku ke-n₂ (contoh: 6)", value="6")

        st.markdown("---")

        n = st.number_input("Masukkan nilai n untuk menghitung Un dan Sn", min_value=1, value=5)

        try:
            u1 = Fraction(u1_str)
            u2 = Fraction(u2_str)
            a, r, error = hitung_a_r_dari_dua_suku(n1, u1, n2, u2)

            if error:
                st.error(error)
            else:
                st.success("✅ Perhitungan berhasil!")
                st.markdown(f"**Suku pertama (a)** = `{a}`")
                st.markdown(f"**Rasio (r)** = `{r}`")

                # Menampilkan Un dan Sn
                un_expr, sn_expr = tampilkan_Un_Sn(a, r, n)
                st.latex(f"U_{{{n}}} = {un_expr}")
                st.latex(f"S_{{{n}}} = {sn_expr}")

                st.markdown("---")
                
                # Fitur jumlah n sampai m
                st.subheader("🔢 Perhitungan jumlah suku ke-n hingga ke-m")

                # Input suku n dan m
                n2_input = st.number_input("Masukkan nilai suku ke-n untuk perhitungan jumlah n sampai m:", min_value=1, step=1, key="n_awal", value=1)
                m_input = st.number_input("Masukkan nilai suku ke-m (lebih dari atau sama dengan n):", min_value=n2_input, step=1, value=n2_input + 1)

                # Perhitungan jumlah n sampai m
                jumlah_nm = hitung_jumlah_n_m_geometri(a, r, n2_input, m_input)
                st.write(f"📌 Jumlah suku dari ke-{n2_input} hingga ke-{m_input} adalah: **{jumlah_nm}**")
        except ValueError:
            st.error("❌ Masukkan pecahan atau angka yang valid!")
            
    elif choice == "Tentang Aplikasi":
        st.subheader("Tentang Aplikasi")
        st.markdown(""" 
        Aplikasi ini adalah portal untuk menghitung deret aritmatika dan deret geometri.  
        Terdapat dua jenis deret yang dapat dihitung melalui aplikasi ini:

        1. **Deret Aritmatika**:  
        Deret dengan selisih tetap antar suku. Aplikasi ini dapat menghitung suku ke-n, jumlah n suku pertama, dan jumlah dari suku ke-n hingga suku ke-m.

        2. **Deret Geometri**:  
        Deret dengan rasio tetap antar suku. Dapat digunakan untuk mencari suku pertama dan rasio dari dua suku acak, serta menghitung suku ke-n dan jumlah n suku.

        Terima kasih telah menggunakan aplikasi ini!
        """)

    elif choice == "Tim Penyusun":
        st.subheader("Tim Penyusun")
        st.markdown("""
        Penyusun Aplikasi ini berisikan 2 orang yaitu:
        1. Hilmi Andika - Aritmatika
        2. Fathur Rizky Ramadhan - Geometri
        """)

if __name__ == '__main__':
    main()
