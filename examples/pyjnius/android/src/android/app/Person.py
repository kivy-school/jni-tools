from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Person"]

class Person(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/Person"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    isBot = JavaMethod("()Z")
    isImportant = JavaMethod("()Z")
    toBuilder = JavaMethod("()Landroid/app/Person$Builder;")
    getName = JavaMethod("()Ljava/lang/CharSequence;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getKey = JavaMethod("()Ljava/lang/String;")
    getUri = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getIcon = JavaMethod("()Landroid/graphics/drawable/Icon;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/Person$Builder"
        __javaconstructor__ = [("()V", False)]
        setImportant = JavaMethod("(Z)Landroid/app/Person$Builder;")
        setBot = JavaMethod("(Z)Landroid/app/Person$Builder;")
        setName = JavaMethod("(Ljava/lang/CharSequence;)Landroid/app/Person$Builder;")
        setIcon = JavaMethod("(Landroid/graphics/drawable/Icon;)Landroid/app/Person$Builder;")
        setUri = JavaMethod("(Ljava/lang/String;)Landroid/app/Person$Builder;")
        setKey = JavaMethod("(Ljava/lang/String;)Landroid/app/Person$Builder;")
        build = JavaMethod("()Landroid/app/Person;")