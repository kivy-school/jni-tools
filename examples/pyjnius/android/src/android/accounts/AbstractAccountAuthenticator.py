from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AbstractAccountAuthenticator"]

class AbstractAccountAuthenticator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/accounts/AbstractAccountAuthenticator"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False)]
    KEY_CUSTOM_TOKEN_EXPIRY = JavaStaticField("Ljava/lang/String;")
    addAccount = JavaMethod("(Landroid/accounts/AccountAuthenticatorResponse;Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Landroid/os/Bundle;)Landroid/os/Bundle;")
    confirmCredentials = JavaMethod("(Landroid/accounts/AccountAuthenticatorResponse;Landroid/accounts/Account;Landroid/os/Bundle;)Landroid/os/Bundle;")
    editProperties = JavaMethod("(Landroid/accounts/AccountAuthenticatorResponse;Ljava/lang/String;)Landroid/os/Bundle;")
    finishSession = JavaMethod("(Landroid/accounts/AccountAuthenticatorResponse;Ljava/lang/String;Landroid/os/Bundle;)Landroid/os/Bundle;")
    getAuthToken = JavaMethod("(Landroid/accounts/AccountAuthenticatorResponse;Landroid/accounts/Account;Ljava/lang/String;Landroid/os/Bundle;)Landroid/os/Bundle;")
    hasFeatures = JavaMethod("(Landroid/accounts/AccountAuthenticatorResponse;Landroid/accounts/Account;[Ljava/lang/String;)Landroid/os/Bundle;")
    isCredentialsUpdateSuggested = JavaMethod("(Landroid/accounts/AccountAuthenticatorResponse;Landroid/accounts/Account;Ljava/lang/String;)Landroid/os/Bundle;")
    startAddAccountSession = JavaMethod("(Landroid/accounts/AccountAuthenticatorResponse;Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Landroid/os/Bundle;)Landroid/os/Bundle;")
    startUpdateCredentialsSession = JavaMethod("(Landroid/accounts/AccountAuthenticatorResponse;Landroid/accounts/Account;Ljava/lang/String;Landroid/os/Bundle;)Landroid/os/Bundle;")
    updateCredentials = JavaMethod("(Landroid/accounts/AccountAuthenticatorResponse;Landroid/accounts/Account;Ljava/lang/String;Landroid/os/Bundle;)Landroid/os/Bundle;")
    getIBinder = JavaMethod("()Landroid/os/IBinder;")
    getAuthTokenLabel = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    addAccountFromCredentials = JavaMethod("(Landroid/accounts/AccountAuthenticatorResponse;Landroid/accounts/Account;Landroid/os/Bundle;)Landroid/os/Bundle;")
    getAccountCredentialsForCloning = JavaMethod("(Landroid/accounts/AccountAuthenticatorResponse;Landroid/accounts/Account;)Landroid/os/Bundle;")
    getAccountRemovalAllowed = JavaMethod("(Landroid/accounts/AccountAuthenticatorResponse;Landroid/accounts/Account;)Landroid/os/Bundle;")