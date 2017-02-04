package core

import "github.com/yurizhykin/peernotify/crypto"

// Put user data into temporary storage and send verification link
// to the email supplied with data
func (n *PeernotifyNode) Register(contact Contact) error {
	return nil
}

// Move user data at 'vid' key in temporary data storage to main storage
func (n *PeernotifyNode) Verify(vid string) error {
	return nil
}

// Lookup user by token and forward message via medium marked as desired
func (n *PeernotifyNode) Forward(token crypto.Token, msg []byte) error {
	return nil
}
