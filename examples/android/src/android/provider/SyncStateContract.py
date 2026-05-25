from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SyncStateContract"]

class SyncStateContract(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/provider/SyncStateContract"
    __javaconstructor__ = [("()V", False)]

    class Columns(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/provider/SyncStateContract/Columns"
        ACCOUNT_NAME = JavaStaticField("Ljava/lang/String;")
        ACCOUNT_TYPE = JavaStaticField("Ljava/lang/String;")
        DATA = JavaStaticField("Ljava/lang/String;")

    class Constants(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/provider/SyncStateContract/Constants"
        __javaconstructor__ = [("()V", False)]
        CONTENT_DIRECTORY = JavaStaticField("Ljava/lang/String;")

    class Helpers(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/provider/SyncStateContract/Helpers"
        __javaconstructor__ = [("()V", False)]
        get = JavaStaticMethod("(Landroid/content/ContentProviderClient;Landroid/net/Uri;Landroid/accounts/Account;)[B")
        set = JavaStaticMethod("(Landroid/content/ContentProviderClient;Landroid/net/Uri;Landroid/accounts/Account;[B)V")
        insert = JavaStaticMethod("(Landroid/content/ContentProviderClient;Landroid/net/Uri;Landroid/accounts/Account;[B)Landroid/net/Uri;")
        update = JavaStaticMethod("(Landroid/content/ContentProviderClient;Landroid/net/Uri;[B)V")
        getWithUri = JavaStaticMethod("(Landroid/content/ContentProviderClient;Landroid/net/Uri;Landroid/accounts/Account;)Landroid/util/Pair;")
        newSetOperation = JavaStaticMethod("(Landroid/net/Uri;Landroid/accounts/Account;[B)Landroid/content/ContentProviderOperation;")
        newUpdateOperation = JavaStaticMethod("(Landroid/net/Uri;[B)Landroid/content/ContentProviderOperation;")