from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VoiceInteractor"]

class VoiceInteractor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/VoiceInteractor"
    getActiveRequests = JavaMethod("()[Landroid/app/VoiceInteractor$Request;")
    submitRequest = JavaMultipleMethod([("(Landroid/app/VoiceInteractor$Request;)Z", False, False), ("(Landroid/app/VoiceInteractor$Request;Ljava/lang/String;)Z", False, False)])
    supportsCommands = JavaMethod("([Ljava/lang/String;)[Z")
    getActiveRequest = JavaMethod("(Ljava/lang/String;)Landroid/app/VoiceInteractor$Request;")
    notifyDirectActionsChanged = JavaMethod("()V")
    registerOnDestroyedCallback = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/lang/Runnable;)Z")
    unregisterOnDestroyedCallback = JavaMethod("(Ljava/lang/Runnable;)Z")
    getPackageName = JavaMethod("()Ljava/lang/String;")
    isDestroyed = JavaMethod("()Z")

    class Request(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/VoiceInteractor$Request"
        onAttached = JavaMethod("(Landroid/app/Activity;)V")
        onDetached = JavaMethod("()V")
        getName = JavaMethod("()Ljava/lang/String;")
        toString = JavaMethod("()Ljava/lang/String;")
        cancel = JavaMethod("()V")
        getActivity = JavaMethod("()Landroid/app/Activity;")
        getContext = JavaMethod("()Landroid/content/Context;")
        onCancel = JavaMethod("()V")

    class Prompt(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/VoiceInteractor$Prompt"
        __javaconstructor__ = [("(Ljava/lang/CharSequence;)V", False), ("([Ljava/lang/CharSequence;Ljava/lang/CharSequence;)V", False)]
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
        PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
        countVoicePrompts = JavaMethod("()I")
        getVisualPrompt = JavaMethod("()Ljava/lang/CharSequence;")
        getVoicePromptAt = JavaMethod("(I)Ljava/lang/CharSequence;")
        toString = JavaMethod("()Ljava/lang/String;")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        describeContents = JavaMethod("()I")

    class PickOptionRequest(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/VoiceInteractor$PickOptionRequest"
        __javaconstructor__ = [("(Landroid/app/VoiceInteractor$Prompt;[Landroid/app/VoiceInteractor$PickOptionRequest$Option;Landroid/os/Bundle;)V", False)]
        onPickOptionResult = JavaMethod("(Z[Landroid/app/VoiceInteractor$PickOptionRequest$Option;Landroid/os/Bundle;)V")

        class Option(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/app/VoiceInteractor$PickOptionRequest$Option"
            __javaconstructor__ = [("(Ljava/lang/CharSequence;I)V", False)]
            CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
            CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
            PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
            getSynonymAt = JavaMethod("(I)Ljava/lang/CharSequence;")
            addSynonym = JavaMethod("(Ljava/lang/CharSequence;)Landroid/app/VoiceInteractor$PickOptionRequest$Option;")
            countSynonyms = JavaMethod("()I")
            getLabel = JavaMethod("()Ljava/lang/CharSequence;")
            setExtras = JavaMethod("(Landroid/os/Bundle;)V")
            getExtras = JavaMethod("()Landroid/os/Bundle;")
            writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
            describeContents = JavaMethod("()I")
            getIndex = JavaMethod("()I")

    class ConfirmationRequest(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/VoiceInteractor$ConfirmationRequest"
        __javaconstructor__ = [("(Landroid/app/VoiceInteractor$Prompt;Landroid/os/Bundle;)V", False)]
        onConfirmationResult = JavaMethod("(ZLandroid/os/Bundle;)V")

    class CompleteVoiceRequest(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/VoiceInteractor$CompleteVoiceRequest"
        __javaconstructor__ = [("(Landroid/app/VoiceInteractor$Prompt;Landroid/os/Bundle;)V", False)]
        onCompleteResult = JavaMethod("(Landroid/os/Bundle;)V")

    class CommandRequest(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/VoiceInteractor$CommandRequest"
        __javaconstructor__ = [("(Ljava/lang/String;Landroid/os/Bundle;)V", False)]
        onCommandResult = JavaMethod("(ZLandroid/os/Bundle;)V")

    class AbortVoiceRequest(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/VoiceInteractor$AbortVoiceRequest"
        __javaconstructor__ = [("(Landroid/app/VoiceInteractor$Prompt;Landroid/os/Bundle;)V", False)]
        onAbortResult = JavaMethod("(Landroid/os/Bundle;)V")