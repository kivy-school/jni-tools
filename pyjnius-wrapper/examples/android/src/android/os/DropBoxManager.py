from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DropBoxManager"]

class DropBoxManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/DropBoxManager"
    __javaconstructor__ = [("()V", False)]
    ACTION_DROPBOX_ENTRY_ADDED = JavaStaticField("Ljava/lang/String;")
    EXTRA_DROPPED_COUNT = JavaStaticField("Ljava/lang/String;")
    EXTRA_TAG = JavaStaticField("Ljava/lang/String;")
    EXTRA_TIME = JavaStaticField("Ljava/lang/String;")
    IS_EMPTY = JavaStaticField("I")
    IS_GZIPPED = JavaStaticField("I")
    IS_TEXT = JavaStaticField("I")
    addText = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    addData = JavaMethod("(Ljava/lang/String;[BI)V")
    addFile = JavaMethod("(Ljava/lang/String;Ljava/io/File;I)V")
    isTagEnabled = JavaMethod("(Ljava/lang/String;)Z")
    getNextEntry = JavaMethod("(Ljava/lang/String;J)Landroid/os/DropBoxManager$Entry;")

    class Entry(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/DropBoxManager/Entry"
        __javaconstructor__ = [("(Ljava/lang/String;J)V", False), ("(Ljava/lang/String;JLjava/lang/String;)V", False), ("(Ljava/lang/String;J[BI)V", False), ("(Ljava/lang/String;JLandroid/os/ParcelFileDescriptor;I)V", False), ("(Ljava/lang/String;JLjava/io/File;I)V", False)]
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        close = JavaMethod("()V")
        getTag = JavaMethod("()Ljava/lang/String;")
        getTimeMillis = JavaMethod("()J")
        getFlags = JavaMethod("()I")
        getText = JavaMethod("(I)Ljava/lang/String;")
        getInputStream = JavaMethod("()Ljava/io/InputStream;")
        describeContents = JavaMethod("()I")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")