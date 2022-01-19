import win32com.client
import os


def main():

    # initiate Outlook app
    outlook = win32com.client.Dispatch('outlook.application')
    mapi = outlook.GetNamespace("MAPI")

    for account in mapi.Accounts:
        print(account.DeliveryStore.DisplayName)

    inbox = mapi.GetDefaultFolder(6)

    messages = inbox.Items
    messages = messages.Restrict("[Subject] = 'Test Email'")

    # directory for file to be saved to
    output_dir = os.getcwd()
    try:
        for message in list(messages):
            try:
                s = message.sender
                for attachment in message.Attachments:
                    attachment.SaveASFile(os.path.join(output_dir, attachment.FileName))
                    print(f"attachment {attachment.FileName} from {s} saved")
            except Exception as e:
                print("error when saving the attachment:" + str(e))
    except Exception as e:
        print("error when processing emails messages:" + str(e))


if __name__ == '__main__':

    main()
