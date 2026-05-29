from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["NfcAdapter"]

class NfcAdapter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/nfc/NfcAdapter"
    ACTION_ADAPTER_STATE_CHANGED = JavaStaticField("Ljava/lang/String;")
    ACTION_CHANGE_TAG_INTENT_PREFERENCE = JavaStaticField("Ljava/lang/String;")
    ACTION_NDEF_DISCOVERED = JavaStaticField("Ljava/lang/String;")
    ACTION_PREFERRED_PAYMENT_CHANGED = JavaStaticField("Ljava/lang/String;")
    ACTION_TAG_DISCOVERED = JavaStaticField("Ljava/lang/String;")
    ACTION_TECH_DISCOVERED = JavaStaticField("Ljava/lang/String;")
    ACTION_TRANSACTION_DETECTED = JavaStaticField("Ljava/lang/String;")
    EXTRA_ADAPTER_STATE = JavaStaticField("Ljava/lang/String;")
    EXTRA_AID = JavaStaticField("Ljava/lang/String;")
    EXTRA_DATA = JavaStaticField("Ljava/lang/String;")
    EXTRA_ID = JavaStaticField("Ljava/lang/String;")
    EXTRA_NDEF_MESSAGES = JavaStaticField("Ljava/lang/String;")
    EXTRA_PREFERRED_PAYMENT_CHANGED_REASON = JavaStaticField("Ljava/lang/String;")
    EXTRA_READER_PRESENCE_CHECK_DELAY = JavaStaticField("Ljava/lang/String;")
    EXTRA_SECURE_ELEMENT_NAME = JavaStaticField("Ljava/lang/String;")
    EXTRA_TAG = JavaStaticField("Ljava/lang/String;")
    FLAG_LISTEN_DISABLE = JavaStaticField("I")
    FLAG_LISTEN_KEEP = JavaStaticField("I")
    FLAG_LISTEN_NFC_PASSIVE_A = JavaStaticField("I")
    FLAG_LISTEN_NFC_PASSIVE_B = JavaStaticField("I")
    FLAG_LISTEN_NFC_PASSIVE_F = JavaStaticField("I")
    FLAG_READER_DISABLE = JavaStaticField("I")
    FLAG_READER_KEEP = JavaStaticField("I")
    FLAG_READER_NFC_A = JavaStaticField("I")
    FLAG_READER_NFC_B = JavaStaticField("I")
    FLAG_READER_NFC_BARCODE = JavaStaticField("I")
    FLAG_READER_NFC_F = JavaStaticField("I")
    FLAG_READER_NFC_V = JavaStaticField("I")
    FLAG_READER_NO_PLATFORM_SOUNDS = JavaStaticField("I")
    FLAG_READER_SKIP_NDEF_CHECK = JavaStaticField("I")
    PREFERRED_PAYMENT_CHANGED = JavaStaticField("I")
    PREFERRED_PAYMENT_LOADED = JavaStaticField("I")
    PREFERRED_PAYMENT_UPDATED = JavaStaticField("I")
    STATE_OFF = JavaStaticField("I")
    STATE_ON = JavaStaticField("I")
    STATE_TURNING_OFF = JavaStaticField("I")
    STATE_TURNING_ON = JavaStaticField("I")
    disable = JavaMethod("()Z")
    disableForegroundDispatch = JavaMethod("(Landroid/app/Activity;)V")
    disableReaderMode = JavaMethod("(Landroid/app/Activity;)V")
    enableForegroundDispatch = JavaMethod("(Landroid/app/Activity;Landroid/app/PendingIntent;[Landroid/content/IntentFilter;[[Ljava/lang/String;)V")
    enableReaderMode = JavaMethod("(Landroid/app/Activity;Landroid/nfc/NfcAdapter$ReaderCallback;ILandroid/os/Bundle;)V")
    getDefaultAdapter = JavaStaticMethod("(Landroid/content/Context;)Landroid/nfc/NfcAdapter;")
    getNfcAntennaInfo = JavaMethod("()Landroid/nfc/NfcAntennaInfo;")
    isObserveModeEnabled = JavaMethod("()Z")
    isObserveModeSupported = JavaMethod("()Z")
    isReaderOptionEnabled = JavaMethod("()Z")
    isReaderOptionSupported = JavaMethod("()Z")
    isSecureNfcEnabled = JavaMethod("()Z")
    isSecureNfcSupported = JavaMethod("()Z")
    isTagIntentAllowed = JavaMethod("()Z")
    isTagIntentAppPreferenceSupported = JavaMethod("()Z")
    resetDiscoveryTechnology = JavaMethod("(Landroid/app/Activity;)V")
    setDiscoveryTechnology = JavaMethod("(Landroid/app/Activity;II)V")
    setObserveModeEnabled = JavaMethod("(Z)Z")
    isEnabled = JavaMethod("()Z")
    ignore = JavaMethod("(Landroid/nfc/Tag;ILandroid/nfc/NfcAdapter$OnTagRemovedListener;Landroid/os/Handler;)Z")
    enable = JavaMethod("()Z")

    class ReaderCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/nfc/NfcAdapter$ReaderCallback"
        onTagDiscovered = JavaMethod("(Landroid/nfc/Tag;)V")

    class OnTagRemovedListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/nfc/NfcAdapter$OnTagRemovedListener"
        onTagRemoved = JavaMethod("()V")

    class OnNdefPushCompleteCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/nfc/NfcAdapter$OnNdefPushCompleteCallback"
        onNdefPushComplete = JavaMethod("(Landroid/nfc/NfcEvent;)V")

    class CreateNdefMessageCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/nfc/NfcAdapter$CreateNdefMessageCallback"
        createNdefMessage = JavaMethod("(Landroid/nfc/NfcEvent;)Landroid/nfc/NdefMessage;")

    class CreateBeamUrisCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/nfc/NfcAdapter$CreateBeamUrisCallback"
        createBeamUris = JavaMethod("(Landroid/nfc/NfcEvent;)[Landroid/net/Uri;")