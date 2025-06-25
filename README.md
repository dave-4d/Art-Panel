# Art Store

This is a simple website to sell my art online. It is built with Python, Flask, and Flask-Mail.

## Features

- View a gallery of artworks loaded from a JSON file
- Purchase an artwork by submitting your name and email
- Receive a thank you email after purchase (sent from the store owner)
- Purchases are saved to a text file

## How to Run

1. **Install requirements**  
   ```
   pip install flask
   pip install flask-mail
   ```

2. **Set up Gmail**  
   - Use your Gmail address and an [App Password](https://support.google.com/accounts/answer/185833?hl=en) in `app.py`.

3. **Add your artworks**  
   - Edit `artworks_data.json` to add your art.

4. **Start the app**  
   ```
   python app.py
   ```

5. **Open in browser**  
   - Go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

## File Structure

```
app.py
artworks_data.json
purchases.txt
templates/
    index.html
    thankyou.html
static/
    css/
        style.css
    images/
```

- **index.html**: This is the main page. It shows all the artworks and has the form for people to buy art.
- **thankyou.html**: This is a simple page that says "Thank you" after someone makes a purchase.

## Notes

- Make sure `artworks_data.json` is valid JSON.
- Emails are sent using the Gmail account you configure in `app.py`.
- Purchases are saved in `purchases.txt`.
