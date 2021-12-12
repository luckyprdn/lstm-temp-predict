def main ():
  import pickle
  import streamlit as st
  # Import library numpy
  import numpy as np
  from tensorflow.keras.models import load_model
  lstm_model = load_model(model.h5)
  st.title('Prediksi suhu di Tanjung Uban, Bintan Utara, Kepulauan Riau dengan LSTM model', anchor=None)
  input = ([[st.number_input('Masukkan suhu yang ingin diprediksi')]])
  
  if st.button("Predict"):
    st.write('Predicting..')
    import time
    my_bar = st.progress(0)

    for percent_complete in range(100):
     time.sleep(0.1)
     my_bar.progress(percent_complete + 2)
    
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler(feature_range=(0,1))           
    temp_scaled = scaler.fit_transform(input) 
    result = lstm_model.predict (temp_scaled)
    result = scaler.inverse_transform(result)
    st.success('Suhu menurut LSTM (Besok)'.format(result))
    st.write(result)

if __name__=='__main__': 
    main()
