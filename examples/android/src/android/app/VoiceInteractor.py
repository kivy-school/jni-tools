from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["VoiceInteractor"]

class VoiceInteractor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/VoiceInteractor"
    submitRequest = JavaMultipleMethod([("(Landroid/app/VoiceInteractor$Request;)Z", False, False), ("(Landroid/app/VoiceInteractor$Request;Ljava/lang/String;)Z", False, False)])
    getActiveRequests = JavaMethod("()[Landroid/app/VoiceInteractor$Request;")
    getActiveRequest = JavaMethod("(Ljava/lang/String;)Landroid/app/VoiceInteractor$Request;")
    supportsCommands = JavaMethod("([Ljava/lang/String;)[Z")
    isDestroyed = JavaMethod("()Z")
    registerOnDestroyedCallback = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/lang/Runnable;)Z")
    unregisterOnDestroyedCallback = JavaMethod("(Ljava/lang/Runnable;)Z")
    notifyDirectActionsChanged = JavaMethod("()V")
    getPackageName = JavaMethod("()Ljava/lang/String;")

    class AbortVoiceRequest(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/VoiceInteractor/AbortVoiceRequest"
        __javaconstructor__ = [("(Landroid/app/VoiceInteractor$Prompt;Landroid/os/Bundle;)V", False)]
        onAbortResult = JavaMethod("(Landroid/os/Bundle;)V")

    class CommandRequest(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/VoiceInteractor/CommandRequest"
        __javaconstructor__ = [("(Ljava/lang/String;Landroid/os/Bundle;)V", False)]
        onCommandResult = JavaMethod("(ZLandroid/os/Bundle;)V")

    class CompleteVoiceRequest(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/VoiceInteractor/CompleteVoiceRequest"
        __javaconstructor__ = [("(Landroid/app/VoiceInteractor$Prompt;Landroid/os/Bundle;)V", False)]
        onCompleteResult = JavaMethod("(Landroid/os/Bundle;)V")

    class ConfirmationRequest(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/VoiceInteractor/ConfirmationRequest"
        __javaconstructor__ = [("(Landroid/app/VoiceInteractor$Prompt;Landroid/os/Bundle;)V", False)]
        onConfirmationResult = JavaMethod("(ZLandroid/os/Bundle;)V")

    class PickOptionRequest(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/VoiceInteractor/PickOptionRequest"
        __javaconstructor__ = [("(Landroid/app/VoiceInteractor$Prompt;[Landroid/app/VoiceInteractor$PickOptionRequest$Option;Landroid/os/Bundle;)V", False)]
        onPickOptionResult = JavaMethod("(Z[Landroid/app/VoiceInteractor$PickOptionRequest$Option;Landroid/os/Bundle;)V")

        class Option(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/app/VoiceInteractor/PickOptionRequest/Option"
            __javaconstructor__ = [("(Ljava/lang/CharSequence;I)V", False)]
            CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
            addSynonym = JavaMethod("(Ljava/lang/CharSequence;)Landroid/app/VoiceInteractor$PickOptionRequest$Option;")
            getLabel = JavaMethod("()Ljava/lang/CharSequence;")
            getIndex = JavaMethod("()I")
            countSynonyms = JavaMethod("()I")
            getSynonymAt = JavaMethod("(I)Ljava/lang/CharSequence;")
            setExtras = JavaMethod("(Landroid/os/Bundle;)V")
            getExtras = JavaMethod("()Landroid/os/Bundle;")
            describeContents = JavaMethod("()I")
            writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Prompt(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/VoiceInteractor/Prompt"
        __javaconstructor__ = [("([Ljava/lang/CharSequence;Ljava/lang/CharSequence;)V", False), ("(Ljava/lang/CharSequence;)V", False)]
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        getVoicePromptAt = JavaMethod("(I)Ljava/lang/CharSequence;")
        countVoicePrompts = JavaMethod("()I")
        getVisualPrompt = JavaMethod("()Ljava/lang/CharSequence;")
        toString = JavaMethod("()Ljava/lang/String;")
        describeContents = JavaMethod("()I")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class Request(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/VoiceInteractor/Request"
        getName = JavaMethod("()Ljava/lang/String;")
        cancel = JavaMethod("()V")
        getContext = JavaMethod("()Landroid/content/Context;")
        getActivity = JavaMethod("()Landroid/app/Activity;")
        onCancel = JavaMethod("()V")
        onAttached = JavaMethod("(Landroid/app/Activity;)V")
        onDetached = JavaMethod("()V")
        toString = JavaMethod("()Ljava/lang/String;")