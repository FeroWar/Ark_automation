import requests

class DiscordWebhook:
    roles = "<@&1290826248603304087>" #<@&1217155884111630569> # Replace with the role ID for pinging

    def __init__(self, webhook_url: str):
        """Initialize with the Discord webhook URL"""
        self.webhook_url = webhook_url

    def LiveHook(self, content, ping):
        """Send a message to the webhook, optionally pinging a role."""
        print(content)  # For debugging

        # Prepare the message content
        if ping:
            print("ping")  # For debugging
            content = f"{content}, {self.roles}"  # Append the role to ping
        else:
            print("else")  # For debugging
            content = f"{content}"  # No ping

        # Build the data payload for the Discord webhook
        data = {
            "content": content  # Message content to send
        }

        # Send the POST request to the Discord webhook
        response = requests.post(self.webhook_url, json=data)

        # Check the response status
        if response.status_code == 204:
            print("Message sent: " + content)
        else:
            print(f"Failed to send message to Discord: {response.text}")

    def AlertDetection(self, New_Logs):
        """Iterates through logs and sends a message based on certain conditions."""
        for log in New_Logs:
            content = log.content.replace("‘", "").replace("’", "").replace('"', "").replace("'","").replace("\n", " ").strip()
            # Extract the content from the TribeLogMessage
            if (("was destroyed" in content and (
                    "Tek" in content or "Metal" in content or "Turret" in content or "Cryofridge" in content)) or
                    ("Your Tribe killed" in content) or
                    ("to public" in content) or
                    ("demolished" in content and (
                            "Tek" in content or "Metal" in content or "Turret" in content or "Vault" in content or "Cryofridge" in content))):
                # Send a ping
                self.LiveHook(log.message().replace("\n", " "), True)
            else:
                print("no ping")
                self.LiveHook(log.message().replace("\n", " "), False)


    def SendMsg(self, text, ping):
        content = f"{text}, {ping}"
        data = {
            "content": content  # Message content to send
        }
        response = requests.post(self.webhook_url, json=data)

        # Check the response status
        if response.status_code == 204:
            print("Message sent: " + content)
        else:
            print(f"Failed to send message to Discord: {response.text}")