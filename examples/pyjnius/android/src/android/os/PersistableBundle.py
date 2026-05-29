from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PersistableBundle"]

class PersistableBundle(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/PersistableBundle"
    __javaconstructor__ = [("()V", False), ("(I)V", False), ("(Landroid/os/PersistableBundle;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    EMPTY = JavaStaticField("Landroid/os/PersistableBundle;")
    clone = JavaMethod("()Ljava/lang/Object;")
    deepCopy = JavaMethod("()Landroid/os/PersistableBundle;")
    putPersistableBundle = JavaMethod("(Ljava/lang/String;Landroid/os/PersistableBundle;)V")
    getPersistableBundle = JavaMethod("(Ljava/lang/String;)Landroid/os/PersistableBundle;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToStream = JavaMethod("(Ljava/io/OutputStream;)V")
    readFromStream = JavaStaticMethod("(Ljava/io/InputStream;)Landroid/os/PersistableBundle;")