from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DropBoxManager"]

class DropBoxManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/DropBoxManager"
    ACTION_DROPBOX_ENTRY_ADDED = JavaStaticField("Ljava/lang/String;")
    EXTRA_DROPPED_COUNT = JavaStaticField("Ljava/lang/String;")
    EXTRA_TAG = JavaStaticField("Ljava/lang/String;")
    EXTRA_TIME = JavaStaticField("Ljava/lang/String;")
    IS_EMPTY = JavaStaticField("I")
    IS_GZIPPED = JavaStaticField("I")
    IS_TEXT = JavaStaticField("I")
    addText = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    addData = JavaMethod("(Ljava/lang/String;[BI)V")
    isTagEnabled = JavaMethod("(Ljava/lang/String;)Z")
    getNextEntry = JavaMethod("(Ljava/lang/String;J)Landroid/os/DropBoxManager$Entry;")
    addFile = JavaMethod("(Ljava/lang/String;Ljava/io/File;I)V")

    class Entry(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/os/DropBoxManager$Entry"
        __javaconstructor__ = [("(Ljava/lang/String;JLjava/lang/String;)V", False), ("(Ljava/lang/String;JLjava/io/File;I)V", False), ("(Ljava/lang/String;J)V", False), ("(Ljava/lang/String;JLandroid/os/ParcelFileDescriptor;I)V", False), ("(Ljava/lang/String;J[BI)V", False)]
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
        PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
        getTimeMillis = JavaMethod("()J")
        close = JavaMethod("()V")
        getInputStream = JavaMethod("()Ljava/io/InputStream;")
        getTag = JavaMethod("()Ljava/lang/String;")
        getFlags = JavaMethod("()I")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        describeContents = JavaMethod("()I")
        getText = JavaMethod("(I)Ljava/lang/String;")