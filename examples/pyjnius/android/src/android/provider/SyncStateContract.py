from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SyncStateContract"]

class SyncStateContract(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/provider/SyncStateContract"
    __javaconstructor__ = [("()V", False)]

    class Helpers(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/provider/SyncStateContract$Helpers"
        __javaconstructor__ = [("()V", False)]
        getWithUri = JavaStaticMethod("(Landroid/content/ContentProviderClient;Landroid/net/Uri;Landroid/accounts/Account;)Landroid/util/Pair;")
        newSetOperation = JavaStaticMethod("(Landroid/net/Uri;Landroid/accounts/Account;[B)Landroid/content/ContentProviderOperation;")
        newUpdateOperation = JavaStaticMethod("(Landroid/net/Uri;[B)Landroid/content/ContentProviderOperation;")
        update = JavaStaticMethod("(Landroid/content/ContentProviderClient;Landroid/net/Uri;[B)V")
        insert = JavaStaticMethod("(Landroid/content/ContentProviderClient;Landroid/net/Uri;Landroid/accounts/Account;[B)Landroid/net/Uri;")
        get = JavaStaticMethod("(Landroid/content/ContentProviderClient;Landroid/net/Uri;Landroid/accounts/Account;)[B")
        set = JavaStaticMethod("(Landroid/content/ContentProviderClient;Landroid/net/Uri;Landroid/accounts/Account;[B)V")

    class Constants(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/provider/SyncStateContract$Constants"
        __javaconstructor__ = [("()V", False)]
        CONTENT_DIRECTORY = JavaStaticField("Ljava/lang/String;")
        ACCOUNT_NAME = JavaStaticField("Ljava/lang/String;")
        ACCOUNT_TYPE = JavaStaticField("Ljava/lang/String;")
        DATA = JavaStaticField("Ljava/lang/String;")
        _COUNT = JavaStaticField("Ljava/lang/String;")
        _ID = JavaStaticField("Ljava/lang/String;")

    class Columns(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/provider/SyncStateContract$Columns"
        ACCOUNT_NAME = JavaStaticField("Ljava/lang/String;")
        ACCOUNT_TYPE = JavaStaticField("Ljava/lang/String;")
        DATA = JavaStaticField("Ljava/lang/String;")
        _COUNT = JavaStaticField("Ljava/lang/String;")
        _ID = JavaStaticField("Ljava/lang/String;")