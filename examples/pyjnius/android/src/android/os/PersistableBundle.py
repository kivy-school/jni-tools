from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PersistableBundle"]

class PersistableBundle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/PersistableBundle"
    __javaconstructor__ = [("(I)V", False), ("(Landroid/os/PersistableBundle;)V", False), ("()V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    EMPTY = JavaStaticField("Landroid/os/PersistableBundle;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    clone = JavaMethod("()Ljava/lang/Object;")
    writeToStream = JavaMethod("(Ljava/io/OutputStream;)V")
    getPersistableBundle = JavaMethod("(Ljava/lang/String;)Landroid/os/PersistableBundle;")
    readFromStream = JavaStaticMethod("(Ljava/io/InputStream;)Landroid/os/PersistableBundle;")
    putPersistableBundle = JavaMethod("(Ljava/lang/String;Landroid/os/PersistableBundle;)V")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    deepCopy = JavaMethod("()Landroid/os/PersistableBundle;")
    describeContents = JavaMethod("()I")