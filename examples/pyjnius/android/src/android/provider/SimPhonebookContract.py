from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SimPhonebookContract"]

class SimPhonebookContract(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/provider/SimPhonebookContract"
    AUTHORITY = JavaStaticField("Ljava/lang/String;")
    AUTHORITY_URI = JavaStaticField("Landroid/net/Uri;")

    class ElementaryFiles(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/provider/SimPhonebookContract/ElementaryFiles"
        CONTENT_ITEM_TYPE = JavaStaticField("Ljava/lang/String;")
        CONTENT_TYPE = JavaStaticField("Ljava/lang/String;")
        CONTENT_URI = JavaStaticField("Landroid/net/Uri;")
        EF_ADN = JavaStaticField("I")
        EF_FDN = JavaStaticField("I")
        EF_SDN = JavaStaticField("I")
        EF_TYPE = JavaStaticField("Ljava/lang/String;")
        EF_UNKNOWN = JavaStaticField("I")
        MAX_RECORDS = JavaStaticField("Ljava/lang/String;")
        NAME_MAX_LENGTH = JavaStaticField("Ljava/lang/String;")
        PHONE_NUMBER_MAX_LENGTH = JavaStaticField("Ljava/lang/String;")
        RECORD_COUNT = JavaStaticField("Ljava/lang/String;")
        SLOT_INDEX = JavaStaticField("Ljava/lang/String;")
        SUBSCRIPTION_ID = JavaStaticField("Ljava/lang/String;")
        getItemUri = JavaStaticMethod("(II)Landroid/net/Uri;")

    class SimRecords(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/provider/SimPhonebookContract/SimRecords"
        CONTENT_ITEM_TYPE = JavaStaticField("Ljava/lang/String;")
        CONTENT_TYPE = JavaStaticField("Ljava/lang/String;")
        ELEMENTARY_FILE_TYPE = JavaStaticField("Ljava/lang/String;")
        ERROR_NAME_UNSUPPORTED = JavaStaticField("I")
        NAME = JavaStaticField("Ljava/lang/String;")
        PHONE_NUMBER = JavaStaticField("Ljava/lang/String;")
        RECORD_NUMBER = JavaStaticField("Ljava/lang/String;")
        SUBSCRIPTION_ID = JavaStaticField("Ljava/lang/String;")
        getContentUri = JavaStaticMethod("(II)Landroid/net/Uri;")
        getItemUri = JavaStaticMethod("(III)Landroid/net/Uri;")
        getEncodedNameLength = JavaStaticMethod("(Landroid/content/ContentResolver;Ljava/lang/String;)I")