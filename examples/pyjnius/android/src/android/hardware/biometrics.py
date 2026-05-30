from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

class BiometricPrompt(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/biometrics/BiometricPrompt"
    AUTHENTICATION_RESULT_TYPE_BIOMETRIC = JavaStaticField("I")
    AUTHENTICATION_RESULT_TYPE_DEVICE_CREDENTIAL = JavaStaticField("I")
    BIOMETRIC_ACQUIRED_GOOD = JavaStaticField("I")
    BIOMETRIC_ACQUIRED_IMAGER_DIRTY = JavaStaticField("I")
    BIOMETRIC_ACQUIRED_INSUFFICIENT = JavaStaticField("I")
    BIOMETRIC_ACQUIRED_PARTIAL = JavaStaticField("I")
    BIOMETRIC_ACQUIRED_TOO_FAST = JavaStaticField("I")
    BIOMETRIC_ACQUIRED_TOO_SLOW = JavaStaticField("I")
    BIOMETRIC_ERROR_CANCELED = JavaStaticField("I")
    BIOMETRIC_ERROR_HW_NOT_PRESENT = JavaStaticField("I")
    BIOMETRIC_ERROR_HW_UNAVAILABLE = JavaStaticField("I")
    BIOMETRIC_ERROR_IDENTITY_CHECK_NOT_ACTIVE = JavaStaticField("I")
    BIOMETRIC_ERROR_LOCKOUT = JavaStaticField("I")
    BIOMETRIC_ERROR_LOCKOUT_PERMANENT = JavaStaticField("I")
    BIOMETRIC_ERROR_NOT_ENABLED_FOR_APPS = JavaStaticField("I")
    BIOMETRIC_ERROR_NO_BIOMETRICS = JavaStaticField("I")
    BIOMETRIC_ERROR_NO_DEVICE_CREDENTIAL = JavaStaticField("I")
    BIOMETRIC_ERROR_NO_SPACE = JavaStaticField("I")
    BIOMETRIC_ERROR_SECURITY_UPDATE_REQUIRED = JavaStaticField("I")
    BIOMETRIC_ERROR_TIMEOUT = JavaStaticField("I")
    BIOMETRIC_ERROR_UNABLE_TO_PROCESS = JavaStaticField("I")
    BIOMETRIC_ERROR_USER_CANCELED = JavaStaticField("I")
    BIOMETRIC_ERROR_VENDOR = JavaStaticField("I")
    BIOMETRIC_NO_AUTHENTICATION = JavaStaticField("J")
    getLogoRes = JavaMethod("()I")
    getLogoBitmap = JavaMethod("()Landroid/graphics/Bitmap;")
    getAllowedAuthenticators = JavaMethod("()I")
    getNegativeButtonText = JavaMethod("()Ljava/lang/CharSequence;")
    isConfirmationRequired = JavaMethod("()Z")
    getDescription = JavaMethod("()Ljava/lang/CharSequence;")
    authenticate = JavaMultipleMethod([("(Landroid/hardware/biometrics/BiometricPrompt$CryptoObject;Landroid/os/CancellationSignal;Ljava/util/concurrent/Executor;Landroid/hardware/biometrics/BiometricPrompt$AuthenticationCallback;)V", False, False), ("(Landroid/os/CancellationSignal;Ljava/util/concurrent/Executor;Landroid/hardware/biometrics/BiometricPrompt$AuthenticationCallback;)V", False, False)])
    getContentView = JavaMethod("()Landroid/hardware/biometrics/PromptContentView;")
    getLogoDescription = JavaMethod("()Ljava/lang/String;")
    getSubtitle = JavaMethod("()Ljava/lang/CharSequence;")
    getTitle = JavaMethod("()Ljava/lang/CharSequence;")

    class CryptoObject(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/biometrics/BiometricPrompt$CryptoObject"
        __javaconstructor__ = [("(Landroid/security/identity/IdentityCredential;)V", False), ("(J)V", False), ("(Landroid/security/identity/PresentationSession;)V", False), ("(Ljava/security/Signature;)V", False), ("(Ljavax/crypto/Cipher;)V", False), ("(Ljavax/crypto/Mac;)V", False)]
        getIdentityCredential = JavaMethod("()Landroid/security/identity/IdentityCredential;")
        getPresentationSession = JavaMethod("()Landroid/security/identity/PresentationSession;")
        getOperationHandle = JavaMethod("()J")
        getMac = JavaMethod("()Ljavax/crypto/Mac;")
        getCipher = JavaMethod("()Ljavax/crypto/Cipher;")
        getSignature = JavaMethod("()Ljava/security/Signature;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/biometrics/BiometricPrompt$Builder"
        __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
        setAllowedAuthenticators = JavaMethod("(I)Landroid/hardware/biometrics/BiometricPrompt$Builder;")
        setConfirmationRequired = JavaMethod("(Z)Landroid/hardware/biometrics/BiometricPrompt$Builder;")
        setLogoBitmap = JavaMethod("(Landroid/graphics/Bitmap;)Landroid/hardware/biometrics/BiometricPrompt$Builder;")
        setDeviceCredentialAllowed = JavaMethod("(Z)Landroid/hardware/biometrics/BiometricPrompt$Builder;")
        setLogoRes = JavaMethod("(I)Landroid/hardware/biometrics/BiometricPrompt$Builder;")
        setNegativeButton = JavaMethod("(Ljava/lang/CharSequence;Ljava/util/concurrent/Executor;Landroid/content/DialogInterface$OnClickListener;)Landroid/hardware/biometrics/BiometricPrompt$Builder;")
        setDescription = JavaMethod("(Ljava/lang/CharSequence;)Landroid/hardware/biometrics/BiometricPrompt$Builder;")
        setContentView = JavaMethod("(Landroid/hardware/biometrics/PromptContentView;)Landroid/hardware/biometrics/BiometricPrompt$Builder;")
        build = JavaMethod("()Landroid/hardware/biometrics/BiometricPrompt;")
        setLogoDescription = JavaMethod("(Ljava/lang/String;)Landroid/hardware/biometrics/BiometricPrompt$Builder;")
        setSubtitle = JavaMethod("(Ljava/lang/CharSequence;)Landroid/hardware/biometrics/BiometricPrompt$Builder;")
        setTitle = JavaMethod("(Ljava/lang/CharSequence;)Landroid/hardware/biometrics/BiometricPrompt$Builder;")

    class AuthenticationResult(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/biometrics/BiometricPrompt$AuthenticationResult"
        getAuthenticationType = JavaMethod("()I")
        getCryptoObject = JavaMethod("()Landroid/hardware/biometrics/BiometricPrompt$CryptoObject;")

    class AuthenticationCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/biometrics/BiometricPrompt$AuthenticationCallback"
        __javaconstructor__ = [("()V", False)]
        onAuthenticationSucceeded = JavaMethod("(Landroid/hardware/biometrics/BiometricPrompt$AuthenticationResult;)V")
        onAuthenticationFailed = JavaMethod("()V")
        onAuthenticationError = JavaMethod("(ILjava/lang/CharSequence;)V")
        onAuthenticationHelp = JavaMethod("(ILjava/lang/CharSequence;)V")

class BiometricManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/biometrics/BiometricManager"
    BIOMETRIC_ERROR_HW_UNAVAILABLE = JavaStaticField("I")
    BIOMETRIC_ERROR_IDENTITY_CHECK_NOT_ACTIVE = JavaStaticField("I")
    BIOMETRIC_ERROR_NONE_ENROLLED = JavaStaticField("I")
    BIOMETRIC_ERROR_NOT_ENABLED_FOR_APPS = JavaStaticField("I")
    BIOMETRIC_ERROR_NO_HARDWARE = JavaStaticField("I")
    BIOMETRIC_ERROR_SECURITY_UPDATE_REQUIRED = JavaStaticField("I")
    BIOMETRIC_NO_AUTHENTICATION = JavaStaticField("J")
    BIOMETRIC_SUCCESS = JavaStaticField("I")
    canAuthenticate = JavaMultipleMethod([("(I)I", False, False), ("()I", False, False)])
    getLastAuthenticationTime = JavaMethod("(I)J")
    getStrings = JavaMethod("(I)Landroid/hardware/biometrics/BiometricManager$Strings;")

    class Strings(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/biometrics/BiometricManager$Strings"
        getButtonLabel = JavaMethod("()Ljava/lang/CharSequence;")
        getPromptMessage = JavaMethod("()Ljava/lang/CharSequence;")
        getSettingName = JavaMethod("()Ljava/lang/CharSequence;")

    class Authenticators(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/biometrics/BiometricManager$Authenticators"
        BIOMETRIC_STRONG = JavaStaticField("I")
        BIOMETRIC_WEAK = JavaStaticField("I")
        DEVICE_CREDENTIAL = JavaStaticField("I")
        IDENTITY_CHECK = JavaStaticField("I")

class PromptContentItemBulletedText(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/biometrics/PromptContentItemBulletedText"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

class PromptContentViewWithMoreOptionsButton(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/biometrics/PromptContentViewWithMoreOptionsButton"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getMoreOptionsButtonListener = JavaMethod("()Landroid/content/DialogInterface$OnClickListener;")
    getDescription = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/biometrics/PromptContentViewWithMoreOptionsButton$Builder"
        __javaconstructor__ = [("()V", False)]
        setMoreOptionsButtonListener = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/content/DialogInterface$OnClickListener;)Landroid/hardware/biometrics/PromptContentViewWithMoreOptionsButton$Builder;")
        setDescription = JavaMethod("(Ljava/lang/String;)Landroid/hardware/biometrics/PromptContentViewWithMoreOptionsButton$Builder;")
        build = JavaMethod("()Landroid/hardware/biometrics/PromptContentViewWithMoreOptionsButton;")

class PromptVerticalListContentView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/biometrics/PromptVerticalListContentView"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getDescription = JavaMethod("()Ljava/lang/String;")
    getListItems = JavaMethod("()Ljava/util/List;")
    getMaxEachItemCharacterNumber = JavaStaticMethod("()I")
    getMaxItemCount = JavaStaticMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/hardware/biometrics/PromptVerticalListContentView$Builder"
        __javaconstructor__ = [("()V", False)]
        setDescription = JavaMethod("(Ljava/lang/String;)Landroid/hardware/biometrics/PromptVerticalListContentView$Builder;")
        addListItem = JavaMultipleMethod([("(Landroid/hardware/biometrics/PromptContentItem;)Landroid/hardware/biometrics/PromptVerticalListContentView$Builder;", False, False), ("(Landroid/hardware/biometrics/PromptContentItem;I)Landroid/hardware/biometrics/PromptVerticalListContentView$Builder;", False, False)])
        build = JavaMethod("()Landroid/hardware/biometrics/PromptVerticalListContentView;")

class PromptContentItemPlainText(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/biometrics/PromptContentItemPlainText"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

class PromptContentView(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/biometrics/PromptContentView"

class PromptContentItem(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/biometrics/PromptContentItem"