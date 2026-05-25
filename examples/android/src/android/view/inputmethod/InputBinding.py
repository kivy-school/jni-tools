from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InputBinding"]

class InputBinding(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/InputBinding"
    __javaconstructor__ = [("(Landroid/view/inputmethod/InputConnection;Landroid/os/IBinder;II)V", False), ("(Landroid/view/inputmethod/InputConnection;Landroid/view/inputmethod/InputBinding;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getConnection = JavaMethod("()Landroid/view/inputmethod/InputConnection;")
    getConnectionToken = JavaMethod("()Landroid/os/IBinder;")
    getUid = JavaMethod("()I")
    getPid = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")