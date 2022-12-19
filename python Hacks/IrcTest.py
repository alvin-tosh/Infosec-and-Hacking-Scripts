from twisted.words.protocols import irc
from twisted.internet import reactor, protocol
import time, sys

class IRCProtocol(irc.IRCClient):

    nickname = 'Spice'
    '''
    nickname	Nickname the client will use.
    password	Password used to log on to the server. May be None.
    realname	Supplied to the server during login as the "Real name" or "ircname". May be None.
    username	Supplied to the server during login as the "User name". May be None
    userinfo	Sent in reply to a USERINFO CTCP query. If None, no USERINFO reply will be sent. "This is used to transmit a string which is settable by the user (and never should be set by the client)."
    fingerReply	Sent in reply to a FINGER CTCP query. If None, no FINGER reply will be sent. (type: Callable or String )
    versionName	CTCP VERSION reply, client name. If None, no VERSION reply will be sent.
    versionNum	CTCP VERSION reply, client version,
    versionEnv	CTCP VERSION reply, environment the client is running in.
    sourceURL	CTCP SOURCE reply, a URL where the source code of this client may be found. If None, no SOURCE reply will be sent.
    lineRate	Minimum delay between lines sent to the server. If None, no delay will be imposed. (type: Number of Seconds. )
    '''
    def __init__(self, factory):
	self.factory = factory

    def connectionMade(self):
        irc.IRCClient.connectionMade(self)

    def connectionLost(self, reason):
        irc.IRCClient.connectionLost(self, reason)
	print "disconnected at %s" % time.asctime(time.localtime(time.time()))

    # Event Oriented

    # Calls for events to the server
	
    def signedOn(self): #Log into the server
        self.join(self.factory.channel)

    def joined(self, channel): 
	print 'Joined to %s ' %(channel)

    def privmsg(self, user, channel, msg): # Private message
	print "%s sends a private message: %s " %(user, msg)

    def action(self, user, channel, msg): # executing an action in the channel
	print "%s action %s: " %(user, msg)

    def userJoined(self, user, channel): # User joins chanel
        print "%s Joined! " %(user)

    def userQuit(self, user, quitMessage): # User leaves chanel
	print '%s Quit... %s' %(user, quitMessage)

    def userRenamed(self, oldname, newname): # changing your username
	print 'Oldnick: %s Newnick: %s ' %(oldname, newname)


class IRCFactory(protocol.ClientFactory):
    def __init__(self, channel):
        self.channel = channel

    def buildProtocol(self, addr):
        p = IRCProtocol(self)
	return p

    def clientConnectionLost(self, connector, reason):
        """Reconnect to server."""
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        reactor.stop()

reactor.connectTCP("irc.freenode.net", 6667, IRCFactory('offsec'))
reactor.run()
