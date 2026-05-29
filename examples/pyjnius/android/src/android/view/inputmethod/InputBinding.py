from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InputBinding"]

class InputBinding(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/InputBinding"
    __javaconstructor__ = [("(Landroid/view/inputmethod/InputConnection;Landroid/os/IBinder;II)V", False), ("(Landroid/view/inputmethod/InputConnection;Landroid/view/inputmethod/InputBinding;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getConnection = JavaMethod("()Landroid/view/inputmethod/InputConnection;")
    getConnectionToken = JavaMethod("()Landroid/os/IBinder;")
    toString = JavaMethod("()Ljava/lang/String;")
    getPid = JavaMethod("()I")
    getUid = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")