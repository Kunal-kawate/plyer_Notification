# plyer_Notification
Desktop Notifications using Plyer · 'plyer' is a really cool module available in Python which is essential for Desktop Notifications.

```markdown
# Notification Sender

This Python script utilizes the `plyer` library to send notifications at regular intervals. It's a simple tool that allows you to display custom notifications on your system.

## Usage

1. Install the `plyer` library using the following command:

    ```bash
    pip install plyer
    ```

2. Update the script with your notification details. Modify the `title` and `message` to customize the notification content. Also, specify the path to your desired notification icon (use only .ico files).

    ```python
    import time
    from plyer import notification

    if __name__ == "__main__":
        while True:
            notification.notify(
                title="KunyaThing",  # Specify your notification title here
                message="Ha mai wahi hu jo fokat ka gyan pel raha hai.",  # Specify your notification message here
                app_icon="C:/Users/Kunal/Desktop/instagram.ico",  # Specify the path to your .ico file
                timeout=5
            )
            # Set the waiting time between notifications (in seconds)
            time.sleep(20)
    ```

3. Run the script to start sending notifications:

    ```bash
    python notifications.py
    ```

## Requirements

- Python 3.x
- `plyer` library

## Note

Make sure to use a valid path to your .ico file for the `app_icon` parameter.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to contribute, report issues, or suggest improvements!

```
