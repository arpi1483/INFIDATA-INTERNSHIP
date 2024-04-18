from streamlit_authenticator.utilities.hasher
import Hasher

hashed_passwords = Hasher(['hope']).generate()
print(hashed_passwords)
