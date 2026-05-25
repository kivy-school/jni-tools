from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ConnectionService"]

class ConnectionService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telecom/ConnectionService"
    __javaconstructor__ = [("()V", False)]
    SERVICE_INTERFACE = JavaStaticField("Ljava/lang/String;")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")
    onUnbind = JavaMethod("(Landroid/content/Intent;)Z")
    createRemoteIncomingConnection = JavaMethod("(Landroid/telecom/PhoneAccountHandle;Landroid/telecom/ConnectionRequest;)Landroid/telecom/RemoteConnection;")
    createRemoteOutgoingConnection = JavaMethod("(Landroid/telecom/PhoneAccountHandle;Landroid/telecom/ConnectionRequest;)Landroid/telecom/RemoteConnection;")
    createRemoteIncomingConference = JavaMethod("(Landroid/telecom/PhoneAccountHandle;Landroid/telecom/ConnectionRequest;)Landroid/telecom/RemoteConference;")
    createRemoteOutgoingConference = JavaMethod("(Landroid/telecom/PhoneAccountHandle;Landroid/telecom/ConnectionRequest;)Landroid/telecom/RemoteConference;")
    conferenceRemoteConnections = JavaMethod("(Landroid/telecom/RemoteConnection;Landroid/telecom/RemoteConnection;)V")
    addConference = JavaMethod("(Landroid/telecom/Conference;)V")
    addExistingConnection = JavaMethod("(Landroid/telecom/PhoneAccountHandle;Landroid/telecom/Connection;)V")
    connectionServiceFocusReleased = JavaMethod("()V")
    getAllConnections = JavaMethod("()Ljava/util/Collection;")
    getAllConferences = JavaMethod("()Ljava/util/Collection;")
    onCreateIncomingConnection = JavaMethod("(Landroid/telecom/PhoneAccountHandle;Landroid/telecom/ConnectionRequest;)Landroid/telecom/Connection;")
    onCreateIncomingConference = JavaMethod("(Landroid/telecom/PhoneAccountHandle;Landroid/telecom/ConnectionRequest;)Landroid/telecom/Conference;")
    onCreateIncomingConnectionFailed = JavaMethod("(Landroid/telecom/PhoneAccountHandle;Landroid/telecom/ConnectionRequest;)V")
    onCreateOutgoingConnectionFailed = JavaMethod("(Landroid/telecom/PhoneAccountHandle;Landroid/telecom/ConnectionRequest;)V")
    onCreateIncomingConferenceFailed = JavaMethod("(Landroid/telecom/PhoneAccountHandle;Landroid/telecom/ConnectionRequest;)V")
    onCreateOutgoingConferenceFailed = JavaMethod("(Landroid/telecom/PhoneAccountHandle;Landroid/telecom/ConnectionRequest;)V")
    onCreateOutgoingConnection = JavaMethod("(Landroid/telecom/PhoneAccountHandle;Landroid/telecom/ConnectionRequest;)Landroid/telecom/Connection;")
    onCreateOutgoingConference = JavaMethod("(Landroid/telecom/PhoneAccountHandle;Landroid/telecom/ConnectionRequest;)Landroid/telecom/Conference;")
    onCreateOutgoingHandoverConnection = JavaMethod("(Landroid/telecom/PhoneAccountHandle;Landroid/telecom/ConnectionRequest;)Landroid/telecom/Connection;")
    onCreateIncomingHandoverConnection = JavaMethod("(Landroid/telecom/PhoneAccountHandle;Landroid/telecom/ConnectionRequest;)Landroid/telecom/Connection;")
    onHandoverFailed = JavaMethod("(Landroid/telecom/ConnectionRequest;I)V")
    onConference = JavaMethod("(Landroid/telecom/Connection;Landroid/telecom/Connection;)V")
    onRemoteConferenceAdded = JavaMethod("(Landroid/telecom/RemoteConference;)V")
    onRemoteExistingConnectionAdded = JavaMethod("(Landroid/telecom/RemoteConnection;)V")
    onConnectionServiceFocusLost = JavaMethod("()V")
    onConnectionServiceFocusGained = JavaMethod("()V")