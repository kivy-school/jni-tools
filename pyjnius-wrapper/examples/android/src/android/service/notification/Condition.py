from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Condition"]

class Condition(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/notification/Condition"
    __javaconstructor__ = [("(Landroid/net/Uri;Ljava/lang/String;I)V", False), ("(Landroid/net/Uri;Ljava/lang/String;II)V", False), ("(Landroid/net/Uri;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;III)V", False), ("(Landroid/net/Uri;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;IIII)V", False), ("(Landroid/os/Parcel;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    FLAG_RELEVANT_ALWAYS = JavaStaticField("I")
    FLAG_RELEVANT_NOW = JavaStaticField("I")
    SCHEME = JavaStaticField("Ljava/lang/String;")
    SOURCE_CONTEXT = JavaStaticField("I")
    SOURCE_SCHEDULE = JavaStaticField("I")
    SOURCE_UNKNOWN = JavaStaticField("I")
    SOURCE_USER_ACTION = JavaStaticField("I")
    STATE_ERROR = JavaStaticField("I")
    STATE_FALSE = JavaStaticField("I")
    STATE_TRUE = JavaStaticField("I")
    STATE_UNKNOWN = JavaStaticField("I")
    flags = JavaField("I")
    icon = JavaField("I")
    id = JavaField("Landroid/net/Uri;")
    line1 = JavaField("Ljava/lang/String;")
    line2 = JavaField("Ljava/lang/String;")
    source = JavaField("I")
    state = JavaField("I")
    summary = JavaField("Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toString = JavaMethod("()Ljava/lang/String;")
    stateToString = JavaStaticMethod("(I)Ljava/lang/String;")
    relevanceToString = JavaStaticMethod("(I)Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    copy = JavaMethod("()Landroid/service/notification/Condition;")
    newId = JavaStaticMethod("(Landroid/content/Context;)Landroid/net/Uri$Builder;")
    isValidId = JavaStaticMethod("(Landroid/net/Uri;Ljava/lang/String;)Z")